# Generated by Django 4.0.3 on 2022-04-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_privacy_user_high_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_helpo_user',
            field=models.BooleanField(default=False),
        ),
    ]
