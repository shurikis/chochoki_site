# Generated by Django 3.2.6 on 2022-02-03 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='games_settings',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='game',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.stage'),
        ),
    ]
