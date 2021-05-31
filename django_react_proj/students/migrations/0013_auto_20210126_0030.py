# Generated by Django 3.0.6 on 2021-01-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20200526_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade_year',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Freshman', 'Freshman'), ('Sophmore', 'Sophmore'), ('Junior', 'Junior'), ('Senior', 'Senior'), ('Master', 'Master'), ('PhD', 'PhD')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
