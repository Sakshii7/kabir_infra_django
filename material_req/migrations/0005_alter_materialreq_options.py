# Generated by Django 4.1.2 on 2022-10-31 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material_req', '0004_rename_materials_materialreq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialreq',
            options={'ordering': ['requisition_date']},
        ),
    ]
