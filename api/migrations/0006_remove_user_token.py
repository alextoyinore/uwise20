# Generated by Django 5.0.6 on 2024-07-09 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
    ]
