# Generated by Django 3.1.1 on 2022-03-02 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Snacks_App', '0002_auto_20220302_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='messages',
            new_name='note',
        ),
    ]