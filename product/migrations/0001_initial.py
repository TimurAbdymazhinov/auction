# Generated by Django 2.2.7 on 2020-05-01 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auctioncore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image')),
                ('auction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lot', to='auctioncore.Auction')),
            ],
        ),
    ]
