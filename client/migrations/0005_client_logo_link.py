# Generated by Django 4.1.5 on 2023-03-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_escalation'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='logo_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]