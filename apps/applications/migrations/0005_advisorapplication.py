# Generated by Django 4.2.10 on 2024-04-09 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_agency_address_agency_document_agency_email_and_more'),
        ('common', '0003_region'),
        ('applications', '0004_application_sent_telegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('RECEIVED', 'Received'), ('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished'), ('CANCELLED', 'Cancelled')], default='RECEIVED', max_length=15, verbose_name='Status')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('who_are_you', models.CharField(max_length=255, verbose_name='Who Are You')),
                ('phone_number', models.CharField(max_length=31, verbose_name='Phone Number')),
                ('agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.agency', verbose_name='Agency')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country', verbose_name='Country')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.region', verbose_name='Region')),
            ],
            options={
                'verbose_name': 'Advisor Application',
                'verbose_name_plural': 'Advisor Applications',
            },
        ),
    ]