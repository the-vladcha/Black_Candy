# Generated by Django 4.0.4 on 2022-04-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telegram_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]