# Generated by Django 4.1.2 on 2022-10-31 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material_req', '0005_alter_materialreq_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialreq',
            options={'ordering': ['name']},
        ),
    ]