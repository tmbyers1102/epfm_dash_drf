# Generated by Django 4.1.5 on 2023-03-15 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Feedo', '0003_feedo_profile_image_url'),
        ('client', '0007_rename_next_monthly_sync_client_next_recurring_sync_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='account_executive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_ae', to='Feedo.feedo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='epfm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_epfm', to='Feedo.feedo'),
        ),
    ]
