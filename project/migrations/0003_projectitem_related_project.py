# Generated by Django 4.1.5 on 2023-01-13 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectitem',
            name='related_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project'),
        ),
    ]