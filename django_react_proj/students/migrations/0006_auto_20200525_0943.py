# Generated by Django 3.0.6 on 2020-05-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20200524_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='job_role',
            field=models.CharField(default='Software Engineer', max_length=30),
        ),
    ]
