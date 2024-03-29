# Generated by Django 4.1.5 on 2023-03-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='ticket_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkin',
            name='waiting_on',
            field=models.CharField(blank=True, choices=[('Me', 'Me'), ('Client', 'Client'), ('Support', 'Support')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
