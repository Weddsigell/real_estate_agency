from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True
    )
    description = models.TextField(
        'Текст объявления',
        blank=True
    )
    price = models.IntegerField(
        'Цена квартиры',
        db_index=True
    )
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True
    )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное'
    )
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4'
    )
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж'
    )
    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True
    )
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True
    )
    new_building = models.BooleanField(
        'Новостройка',
        null=True,
        db_index=True
    )
    likes = models.ManyToManyField(
        User,
        verbose_name='лайки',
        related_name='flats',
        blank=True,
    )
    has_balcony = models.BooleanField(
        'Наличие балкона',
        null=True,
        blank=True,
        db_index=True
    )
    active = models.BooleanField(
        'Активно-ли объявление',
        db_index=True
    )
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='жалоба',
        related_name='complaints',
        on_delete=models.SET_NULL,
        null=True
    )
    report = models.TextField(
        'текст жалобы',
        null=False
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name='квартира',
        related_name='complaints'
    )

    def __str__(self):
        return f'жалоба на {self.flat}'

class Owner(models.Model):
    owner = models.CharField(
        verbose_name='ФИО владельца',
        max_length=200,
        null=False,
        db_index=True
    )
    owners_phonenumber = PhoneNumberField(
        verbose_name='Номер владельца',
        max_length=12,
        null=True,
        region='RU'
    )
    flats = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры',
        related_name='owners',
        blank=True,
    )

    def __str__(self):
        return f'{self.owner}'
