# Generated by Django 4.1.5 on 2023-03-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0010_alter_update_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='ticket_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
