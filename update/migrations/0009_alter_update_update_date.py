# Generated by Django 4.1.5 on 2023-03-01 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0008_alter_update_update_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='update_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]