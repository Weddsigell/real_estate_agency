# Generated by Django 5.1.7 on 2025-03-10 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_remove_flat_owner_remove_flat_owner_pure_phone_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.flat', verbose_name='квартира'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='жалоба'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='flats', to=settings.AUTH_USER_MODEL, verbose_name='лайки'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Новостройка'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.flat', verbose_name='Квартиры'),
        ),
    ]
