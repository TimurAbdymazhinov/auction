# Generated by Django 2.2.7 on 2020-05-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctioncore', '0011_auto_20200514_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='increment',
            field=models.IntegerField(blank=True, choices=[(1, '1%'), (2, '2%'), (3, '3%'), (4, '4%'), (5, '5%')], null=True),
        ),
    ]
