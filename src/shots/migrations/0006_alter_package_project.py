# Generated by Django 5.1.1 on 2024-09-20 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0005_package_earliest_delivery_package_latest_delivery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shots.project'),
        ),
    ]
