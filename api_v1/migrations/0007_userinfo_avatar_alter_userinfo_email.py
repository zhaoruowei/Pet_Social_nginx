# Generated by Django 4.0.6 on 2022-07-23 16:06

import api_v1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0006_userinfo_age_userinfo_email_userinfo_join_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to=api_v1.models.avatar_dic_path, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=256, null=True, verbose_name='email'),
        ),
    ]
