# Generated by Django 2.2.2 on 2019-08-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='postcoment',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
