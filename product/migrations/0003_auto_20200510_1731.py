# Generated by Django 2.2.7 on 2020-05-10 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200509_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='product.Product'),
        ),
    ]
