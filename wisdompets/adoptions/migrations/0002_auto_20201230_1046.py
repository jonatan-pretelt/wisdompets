# Generated by Django 3.1.4 on 2020-12-30 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='submission',
            new_name='submission_date',
        ),
    ]
