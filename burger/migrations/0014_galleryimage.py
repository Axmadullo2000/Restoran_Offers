# Generated by Django 3.2.6 on 2021-08-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0013_singleblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.FileField(default=None, upload_to='img/burgers/')),
            ],
        ),
    ]