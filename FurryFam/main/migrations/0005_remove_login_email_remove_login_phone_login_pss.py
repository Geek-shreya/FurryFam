# Generated by Django 4.2.1 on 2024-04-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_login_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='email',
        ),
        migrations.RemoveField(
            model_name='login',
            name='phone',
        ),
        migrations.AddField(
            model_name='login',
            name='pss',
            field=models.CharField(default='', max_length=20),
        ),
    ]