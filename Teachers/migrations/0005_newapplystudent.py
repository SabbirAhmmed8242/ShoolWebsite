# Generated by Django 5.1.7 on 2025-05-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0004_teacherdata_delete_teacherdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewApplyStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mother', models.CharField(max_length=30)),
                ('father', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('cls', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='NewStudentApplys/')),
            ],
        ),
    ]
