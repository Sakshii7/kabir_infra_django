# Generated by Django 4.1.2 on 2022-11-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_supervisior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisior',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
