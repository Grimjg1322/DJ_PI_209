# Generated by Django 4.2.5 on 2023-11-16 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='dipolom_red',
            new_name='diplom_red',
        ),
    ]