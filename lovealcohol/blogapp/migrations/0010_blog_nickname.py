# Generated by Django 2.2.2 on 2019-08-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='nickname',
            field=models.TextField(max_length=15, null=True),
        ),
    ]