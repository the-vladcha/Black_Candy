# Generated by Django 4.0.4 on 2022-04-16 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0004_usersession_limit_price_usersession_limit_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersession',
            old_name='limit_time',
            new_name='notification_time',
        ),
    ]