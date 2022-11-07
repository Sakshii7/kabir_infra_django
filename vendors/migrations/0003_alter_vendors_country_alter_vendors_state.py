# Generated by Django 4.1.2 on 2022-11-07 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_alter_city_zipcode'),
        ('vendors', '0002_alter_vendors_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.country'),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.state'),
        ),
    ]