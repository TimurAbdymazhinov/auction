# Generated by Django 2.2.7 on 2020-05-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=models.TextField(blank=True, default=True, null=True),
        ),
    ]
