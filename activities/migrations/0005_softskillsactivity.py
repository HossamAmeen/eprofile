# Generated by Django 5.0.4 on 2024-06-13 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_studentactivity_score_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftSkillsActivity',
            fields=[
                ('studentactivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.studentactivity')),
                ('name', models.CharField(max_length=150)),
            ],
            bases=('activities.studentactivity',),
        ),
    ]