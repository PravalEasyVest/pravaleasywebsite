# Generated by Django 2.2.5 on 2019-09-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='readtime',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
