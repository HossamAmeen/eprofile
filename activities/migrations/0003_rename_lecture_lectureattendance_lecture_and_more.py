# Generated by Django 5.0.4 on 2024-05-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_exam_examscore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lectureattendance',
            old_name='Lecture',
            new_name='lecture',
        ),
        migrations.AddField(
            model_name='lectureattendance',
            name='is_present',
            field=models.BooleanField(default=False, null=True),
        ),
    ]