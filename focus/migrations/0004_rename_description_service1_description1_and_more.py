# Generated by Django 4.2 on 2024-09-13 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0003_service1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service1',
            old_name='description',
            new_name='description1',
        ),
        migrations.RenameField(
            model_name='service1',
            old_name='icon',
            new_name='icon1',
        ),
        migrations.RenameField(
            model_name='service1',
            old_name='title',
            new_name='title1',
        ),
    ]
