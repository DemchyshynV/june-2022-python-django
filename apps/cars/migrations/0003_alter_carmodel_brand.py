# Generated by Django 4.1.3 on 2022-11-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_created_at_carmodel_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
