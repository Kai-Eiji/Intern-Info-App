# Generated by Django 3.0.6 on 2021-01-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20210127_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade_year',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Freshman', 'Freshman'), ('Sophmore', 'Sophmore'), ('Junior', 'Junior'), ('Senior', 'Senior'), ('Master', 'Master'), ('PhD', 'PhD')], default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]