# Generated by Django 4.1.4 on 2023-01-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='data',
            field=models.JSONField(default={'size': []}, null=True),
        ),
    ]
