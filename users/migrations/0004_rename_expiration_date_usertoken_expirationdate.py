# Generated by Django 5.0.4 on 2024-05-19 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usertoken_delete_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertoken',
            old_name='expiration_date',
            new_name='expirationdate',
        ),
    ]
