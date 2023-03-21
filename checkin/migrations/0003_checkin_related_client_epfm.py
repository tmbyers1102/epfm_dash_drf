# Generated by Django 4.1.5 on 2023-03-08 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Feedo', '0003_feedo_profile_image_url'),
        ('checkin', '0002_checkin_ticket_link_checkin_waiting_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='related_client_epfm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checkin_feedo', to='Feedo.feedo'),
        ),
    ]
