# Generated by Django 4.2.1 on 2024-04-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=80)),
                ('phone', models.CharField(default='', max_length=80)),
                ('desc', models.CharField(default='', max_length=800)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
