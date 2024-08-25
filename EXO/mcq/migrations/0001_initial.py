# Generated by Django 4.0.6 on 2022-08-13 19:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examID', models.CharField(default=uuid.uuid4, max_length=50)),
                ('CohortID', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=300)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
    ]
