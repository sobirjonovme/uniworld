# Generated by Django 4.2.10 on 2024-07-31 10:29

from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0006_alter_universitycourse_duration'),
        ('applications', '0008_advisorapplication_sent_telegram'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisorapplication',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='advisorapplication',
            name='certificates',
            field=django_jsonform.models.fields.JSONField(blank=True, null=True, verbose_name='Certificates'),
        ),
        migrations.AddField(
            model_name='advisorapplication',
            name='current_education_level',
            field=models.CharField(blank=True, choices=[('HIGH_SCHOOL', 'High School'), ('BACHELOR', 'Bachelor')], max_length=31, null=True, verbose_name='Current Education Level'),
        ),
        migrations.AddField(
            model_name='advisorapplication',
            name='gpa',
            field=models.CharField(blank=True, max_length=63, null=True, verbose_name='GPA'),
        ),
        migrations.AddField(
            model_name='advisorapplication',
            name='needed_education_level',
            field=models.CharField(blank=True, choices=[('BACHELOR', 'Bachelor'), ('MASTER', 'Master')], max_length=31, null=True, verbose_name='Needed Education Level'),
        ),
        migrations.AddField(
            model_name='advisorapplication',
            name='needed_specialty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='universities.specialty', verbose_name='Needed Specialty'),
        ),
        migrations.AddField(
            model_name='advisorapplication',
            name='type',
            field=models.CharField(choices=[('ELIGIBILITY_CHECK', 'Eligibility Check'), ('SPEAK_WITH_ADVISOR', 'Speak with Advisor')], default='SPEAK_WITH_ADVISOR', max_length=31, verbose_name='Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advisorapplication',
            name='who_are_you',
            field=models.CharField(blank=True, choices=[('STUDENT', 'Student'), ('PARENT', 'Parent')], max_length=31, null=True, verbose_name='Who Are You'),
        ),
    ]
