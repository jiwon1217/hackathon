# Generated by Django 2.2.4 on 2019-08-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20190808_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]