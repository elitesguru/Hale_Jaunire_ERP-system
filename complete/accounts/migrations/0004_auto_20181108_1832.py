# Generated by Django 2.1.3 on 2018-11-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
