# Generated by Django 5.1.7 on 2025-05-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='secret_number_and_NID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_number', models.CharField(max_length=18)),
                ('NID', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='secret_number',
        ),
    ]
