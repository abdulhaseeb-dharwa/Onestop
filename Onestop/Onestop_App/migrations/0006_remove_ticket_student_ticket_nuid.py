# Generated by Django 4.2.5 on 2023-12-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Onestop_App', '0005_remove_faculty_course_remove_faculty_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='student',
        ),
        migrations.AddField(
            model_name='ticket',
            name='nuid',
            field=models.CharField(default='KXX0000', max_length=7),
        ),
    ]
