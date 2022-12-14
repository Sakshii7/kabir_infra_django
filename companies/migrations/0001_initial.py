# Generated by Django 4.1.2 on 2022-11-09 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0005_alter_city_zipcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('street2', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('gstin', models.CharField(max_length=20)),
                ('pan_no', models.CharField(max_length=20)),
                ('cin_no', models.CharField(max_length=20)),
                ('company_registry', models.CharField(max_length=200)),
                ('owner_name', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.state')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
