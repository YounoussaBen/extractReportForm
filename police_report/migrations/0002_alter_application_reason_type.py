# Generated by Django 3.2.17 on 2024-03-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='reason_type',
            field=models.CharField(max_length=255),
        ),
    ]