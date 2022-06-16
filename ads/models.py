from django.db import models

class Ads(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=10)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()

class Categories(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=1000)
    lat = models.FloatField()
    lng = models.FloatField()

class User(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=10)
    age = models.BigIntegerField()
    location_id = models.BigIntegerField()
