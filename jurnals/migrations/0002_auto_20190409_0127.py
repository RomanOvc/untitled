# Generated by Django 2.2 on 2019-04-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurnals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.FileField(upload_to='post/', verbose_name='Image'),
        ),
    ]