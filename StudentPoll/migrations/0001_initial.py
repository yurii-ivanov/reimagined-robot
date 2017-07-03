# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DeaneryResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField(default=0)),
                ('amount', models.SmallIntegerField(default=0)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveSmallIntegerField(default=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lName', models.CharField(max_length=50)),
                ('fName', models.CharField(max_length=50)),
                ('mName', models.CharField(max_length=50)),
                ('subject', models.ManyToManyField(to='StudentPoll.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startYear', models.SmallIntegerField(default=2017)),
                ('endYear', models.SmallIntegerField(default=2018)),
                ('half', models.SmallIntegerField(choices=[(2, '2'), (1, '1')], default=1)),
                ('isActive', models.BooleanField(default=False, verbose_name='Активувати')),
                ('categories', models.ManyToManyField(to='StudentPoll.Category')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='VoteCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.PositiveSmallIntegerField(default=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Group')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Vote')),
            ],
        ),
        migrations.CreateModel(
            name='VoteResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Category')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Teacher')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Vote')),
            ],
        ),
        migrations.AddField(
            model_name='studyplan',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Subject'),
        ),
        migrations.AddField(
            model_name='deaneryresult',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentPoll.Vote'),
        ),
    ]
