# Generated by Django 3.0.6 on 2020-05-26 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200525_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='housing_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
