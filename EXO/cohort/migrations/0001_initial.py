# Generated by Django 4.0.6 on 2022-08-22 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cohort',
            fields=[
                ('CohortID', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('CohortName', models.CharField(max_length=30)),
                ('Admin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('examID', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExamInfo',
            fields=[
                ('examID', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('examName', models.CharField(max_length=30)),
                ('examType', models.CharField(max_length=20)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort.cohort')),
            ],
        ),
        migrations.CreateModel(
            name='cohortInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('MemberStatus', models.CharField(max_length=60)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort.cohort')),
            ],
            options={
                'unique_together': {('cohort', 'Member')},
            },
        ),
    ]
