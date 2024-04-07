# Generated by Django 4.2.10 on 2024-04-07 05:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_region'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='agency',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Document'),
        ),
        migrations.AddField(
            model_name='agency',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='agency',
            name='founded_year',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Founded year'),
        ),
        migrations.AddField(
            model_name='agency',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.CreateModel(
            name='AgencyCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='organizations.agency', verbose_name='Agency')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agencies', to='common.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Agency Country',
                'verbose_name_plural': 'Agency Countries',
                'unique_together': {('agency', 'country')},
            },
        ),
    ]
