# Generated by Django 4.2.11 on 2024-04-29 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='addresss',
            new_name='address',
        ),
    ]
