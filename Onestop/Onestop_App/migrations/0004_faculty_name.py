# Generated by Django 4.2.5 on 2023-12-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Onestop_App', '0003_alter_section_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='name',
            field=models.CharField(default='None', max_length=30),
        ),
    ]