# Generated by Django 2.1.3 on 2018-11-18 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20181118_1832'),
        ('assignments', '0003_remove_tasklist_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='work',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Todolist'),
        ),
    ]
