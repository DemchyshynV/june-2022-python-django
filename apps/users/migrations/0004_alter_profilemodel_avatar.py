# Generated by Django 4.1.4 on 2022-12-07 18:11

from django.db import migrations, models

import apps.users.services


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profilemodel_avatar_alter_profilemodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=apps.users.services.upload_avatar),
        ),
    ]
