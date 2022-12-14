# Generated by Django 4.1.2 on 2022-10-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('street2', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
