# Generated by Django 2.2.7 on 2020-05-25 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0010_auto_20200525_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order']},
        ),
    ]
