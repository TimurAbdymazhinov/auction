# Generated by Django 2.2.7 on 2020-05-10 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20200510_1731'),
        ('auctioncore', '0005_auto_20200509_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='category.SubCategory'),
            preserve_default=False,
        ),
    ]
