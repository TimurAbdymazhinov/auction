# Generated by Django 2.2.7 on 2020-05-22 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0005_delete_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
