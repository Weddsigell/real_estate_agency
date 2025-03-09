# Generated by Django 5.1.7 on 2025-03-09 10:30
import phonenumbers
from django.db import migrations


def write_in_number_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        parsed_number  = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            flat.owner_pure_phone = flat.owners_phonenumber
        else:
            flat.owner_pure_phone = None

        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_alter_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(write_in_number_phone),
    ]
