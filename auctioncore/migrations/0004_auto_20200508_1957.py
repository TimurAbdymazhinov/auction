# Generated by Django 2.2.7 on 2020-05-08 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctioncore', '0003_auto_20200508_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='last_bit',
            new_name='last_bet',
        ),
    ]
