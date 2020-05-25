# Generated by Django 2.2.7 on 2020-05-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0009_auto_20200522_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=3, unique=True),
            preserve_default=False,
        ),
    ]
