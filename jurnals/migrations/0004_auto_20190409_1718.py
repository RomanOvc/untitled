# Generated by Django 2.2 on 2019-04-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurnals', '0003_auto_20190409_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
