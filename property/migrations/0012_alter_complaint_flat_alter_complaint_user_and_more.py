# Generated by Django 5.1.7 on 2025-03-09 11:18

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20250309_1530'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint', to='property.flat', verbose_name='квартира'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaint', to=settings.AUTH_USER_MODEL, verbose_name='жалоба'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='flats', to=settings.AUTH_USER_MODEL, verbose_name='лайки'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=12, null=True, region='RU', verbose_name='Номер владельца')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.flat', verbose_name='Квартиры')),
            ],
        ),
    ]
