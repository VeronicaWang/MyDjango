# Generated by Django 3.0.6 on 2020-05-28 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zhihu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='ceshi',
        ),
        migrations.RenameField(
            model_name='ceshi',
            old_name='name',
            new_name='name_title',
        ),
    ]