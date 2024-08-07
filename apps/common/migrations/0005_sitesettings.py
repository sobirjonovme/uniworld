# Generated by Django 4.2.10 on 2024-04-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_aboutus_privacypolicy_termsandconditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advice_requests_chat_id', models.CharField(blank=True, help_text='Chat ID in Telegram', max_length=255, null=True, verbose_name='Advice requests Chat ID')),
            ],
            options={
                'verbose_name': 'Site settings',
                'verbose_name_plural': 'Site settings',
            },
        ),
    ]
