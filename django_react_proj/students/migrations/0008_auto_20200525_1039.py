# Generated by Django 3.0.6 on 2020-05-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200525_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='prev_exp_num',
            field=models.CharField(max_length=10),
        ),
    ]
