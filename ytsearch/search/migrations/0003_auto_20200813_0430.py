# Generated by Django 3.0.8 on 2020-08-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_savedvids_videoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedvids',
            name='title',
            field=models.TextField(),
        ),
    ]