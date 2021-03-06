# Generated by Django 2.2.7 on 2020-05-01 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='Город')),
                ('is_active', models.BooleanField(default=True)),
                ('is_done', models.BooleanField(default=False)),
                ('start_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='category.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='auctioncore.Auction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
