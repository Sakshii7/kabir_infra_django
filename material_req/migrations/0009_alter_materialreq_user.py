# Generated by Django 4.1.2 on 2022-11-10 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_users_is_add_sites_and_vendors_and_more'),
        ('material_req', '0008_remove_materialreq_user_id_materialreq_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialreq',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users'),
        ),
    ]
