# Generated by Django 3.2.6 on 2021-08-16 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0002_alter_firstmodel_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='firstModel',
            new_name='CarouselContent',
        ),
    ]
