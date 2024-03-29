# Generated by Django 4.2.10 on 2024-03-29 12:38

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0005_university_address_university_full_scolarship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='universities/images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='university',
            name='logo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='universities/logos/', verbose_name='Logo'),
        ),
    ]