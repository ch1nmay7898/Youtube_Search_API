# Generated by Django 3.0.8 on 2020-08-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20200813_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedvids',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='savedvids',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
