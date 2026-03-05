from random import choices

from django.db import models
from django.contrib.auth.models import User


class Pilot(models.Model):
    RANK_CHOICES = [
        ('J', 'Junior'),
        ('I','Intermediate'),
        ('S','Senior')
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_of_birth=models.IntegerField()
    total_flight_hours = models.IntegerField(null=True,blank=True)
    rank = models.CharField(max_length=1,choices=RANK_CHOICES)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Baloon(models.Model):
    TYPE_CHOICES = [
        ('S', 'Small Baloon'),
        ('M', 'Medium Baloon'),
        ('L', 'Large Baloon'),
    ]
    name = models.CharField(max_length=100)
    type=models.CharField(max_length=1,choices=TYPE_CHOICES)
    manufacturer=models.CharField(max_length=100)
    max_passengers=models.IntegerField()
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return f'{self.name} {self.manufacturer}'


class Airline(models.Model):
    name=models.CharField(max_length=100)
    year_founded = models.IntegerField()
    outside_Europe = models.BooleanField()

    def __str__(self):
        return f'{self.name} {self.year_founded}'


class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.airline} {self.pilot}'


class Flight(models.Model):
    code=models.CharField(max_length=100,unique=True)
    take_off_airport=models.CharField(max_length=100,null=True,blank=True)
    landing_airport=models.CharField(max_length=100,null=True,blank=True)
    user  =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    balloon = models.ForeignKey(Baloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} {self.take_off_airport} {self.landing_airport}'
