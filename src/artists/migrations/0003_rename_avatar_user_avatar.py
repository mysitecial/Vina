# Generated by Django 5.1.1 on 2024-09-20 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_user_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Avatar',
            new_name='avatar',
        ),
    ]