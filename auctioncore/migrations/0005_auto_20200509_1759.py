# Generated by Django 2.2.7 on 2020-05-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctioncore', '0004_auto_20200508_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acomments',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='auction',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]