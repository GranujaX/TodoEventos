# Generated by Django 4.2.4 on 2023-10-30 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_delete_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nickname',
            new_name='username',
        ),
    ]
