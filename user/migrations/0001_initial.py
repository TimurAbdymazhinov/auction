# Generated by Django 3.0.3 on 2020-03-04 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_client', models.BooleanField(default=False)),
                ('is_auction_owner', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='user/profile_photo.png', null=True, upload_to='user', verbose_name='Фотография')),
                ('country', models.CharField(blank=True, max_length=200, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='Город')),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
