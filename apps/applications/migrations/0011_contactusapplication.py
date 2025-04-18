# Generated by Django 4.2.10 on 2025-02-06 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_agency_address_agency_document_agency_email_and_more'),
        ('applications', '0010_alter_advisorapplication_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('telegram_username', models.CharField(max_length=255, verbose_name='Telegram Username')),
                ('phone_number', models.CharField(max_length=31, verbose_name='Phone Number')),
                ('inquiry_type', models.CharField(choices=[('NEED_HELP', 'Need Help'), ('COMPLAINT', 'Complaint')], max_length=31, verbose_name='Inquiry Type')),
                ('message', models.TextField(verbose_name='Message')),
                ('consulting_agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.agency', verbose_name='Consulting Agency')),
            ],
            options={
                'verbose_name': 'Contact Us Application',
                'verbose_name_plural': 'Contact Us Applications',
            },
        ),
    ]
