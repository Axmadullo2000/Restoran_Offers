# Generated by Django 3.2.6 on 2021-08-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0008_auto_20210816_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburgerclient',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]