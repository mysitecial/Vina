# Generated by Django 5.1.1 on 2024-09-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0011_alter_shot_shot_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shot',
            name='annotations',
            field=models.ImageField(blank=True, null=True, upload_to='annotations/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]