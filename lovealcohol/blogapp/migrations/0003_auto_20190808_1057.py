# Generated by Django 2.2.4 on 2019-08-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
