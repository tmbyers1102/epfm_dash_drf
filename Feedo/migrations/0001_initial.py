# Generated by Django 4.1.5 on 2023-03-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('role', models.CharField(choices=[('EPFM', 'Epfm'), ('OPS', 'Ops'), ('OTHER', 'Other')], default='EPFM', max_length=50)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
