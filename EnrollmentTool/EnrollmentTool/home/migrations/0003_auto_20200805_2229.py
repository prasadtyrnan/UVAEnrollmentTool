# Generated by Django 3.1 on 2020-08-05 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200805_2220'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discussions_and_Labs',
            new_name='Discussion_or_Lab',
        ),
        migrations.RenameModel(
            old_name='Lectures',
            new_name='Lecture',
        ),
    ]