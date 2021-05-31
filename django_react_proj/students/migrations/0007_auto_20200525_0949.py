# Generated by Django 3.0.6 on 2020-05-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20200525_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='perks',
        ),
        migrations.AddField(
            model_name='student',
            name='housing',
            field=models.CharField(default='No Housing Support', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='housing_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='jobs_applied',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
