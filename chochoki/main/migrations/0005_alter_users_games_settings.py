# Generated by Django 3.2.6 on 2022-01-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220130_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='games_settings',
            field=models.TextField(),
        ),
    ]
