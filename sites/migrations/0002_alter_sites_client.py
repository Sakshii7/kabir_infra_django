# Generated by Django 4.1.2 on 2022-11-02 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('sites', '0001_app_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='clients.clients'),
        ),
    ]
