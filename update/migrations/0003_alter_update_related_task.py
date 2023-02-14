# Generated by Django 4.1.5 on 2023-02-12 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_alter_task_due_date'),
        ('update', '0002_update_related_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='related_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_update', to='task.task'),
        ),
    ]