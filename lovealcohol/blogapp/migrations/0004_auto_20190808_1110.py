# Generated by Django 2.2.4 on 2019-08-08 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20190808_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_data',
            field=models.DateTimeField(null=True, verbose_name='data published'),
        ),
    ]