# Generated by Django 4.2.10 on 2024-04-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_alter_advisorapplication_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisorapplication',
            name='sent_telegram',
            field=models.BooleanField(default=False, verbose_name='Sent Telegram'),
        ),
    ]