# Generated by Django 5.0.4 on 2024-05-08 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('approve_status', models.CharField(choices=[('pending', 'Pending'), ('accept', 'Accept'), ('reject', 'Reject')], default='pending', max_length=30)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('score', models.IntegerField(default=0)),
                ('staff_member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.staffmember')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicAttendance',
            fields=[
                ('studentactivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.studentactivity')),
                ('place', models.CharField(max_length=100)),
            ],
            bases=('activities.studentactivity',),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('studentactivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.studentactivity')),
                ('topic', models.CharField(max_length=100)),
            ],
            bases=('activities.studentactivity',),
        ),
        migrations.CreateModel(
            name='OperationAttendance',
            fields=[
                ('studentactivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.studentactivity')),
                ('place', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
                ('procedure', models.CharField(max_length=100)),
            ],
            bases=('activities.studentactivity',),
        ),
        migrations.CreateModel(
            name='ShiftAttendance',
            fields=[
                ('studentactivity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='activities.studentactivity')),
                ('place', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=20)),
            ],
            bases=('activities.studentactivity',),
        ),
        migrations.CreateModel(
            name='LectureAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.student')),
                ('Lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.lecture')),
            ],
        ),
    ]
