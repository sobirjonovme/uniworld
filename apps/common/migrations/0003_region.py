# Generated by Django 4.2.10 on 2024-03-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_country_name_en_country_name_ru_country_name_uz_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
    ]
