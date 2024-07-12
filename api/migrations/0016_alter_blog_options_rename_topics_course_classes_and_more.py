# Generated by Django 5.0.6 on 2024-07-12 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_course_intro_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'managed': True, 'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='topics',
            new_name='classes',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='objectives',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterModelTable(
            name='blog',
            table='Blogs',
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.JSONField()),
                ('date', models.DateTimeField()),
                ('slug', models.SlugField(null=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'db_table': 'Messages',
                'managed': True,
            },
        ),
    ]