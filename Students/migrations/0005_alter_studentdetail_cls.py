# Generated by Django 5.1.7 on 2025-05-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0004_studentdetail_delete_studentdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='cls',
            field=models.CharField(max_length=8),
        ),
    ]
