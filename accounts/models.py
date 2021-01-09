from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class User(AbstractUser):
    is_customer = models.BooleanField('chef status', default=False)
    is_chef = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile_phone = models.IntegerField(default=None)
    country = CountryField()
    is_active = models.BooleanField(default=None)


class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile_phone = models.IntegerField(default=None)
    country = CountryField()
    instagram_account = models.CharField(max_length=100, default=None)
    youtube_account = models.CharField(max_length=100, default=None)
    is_active = models.BooleanField(default=None)

    def __str__(self):
        return self.user.username


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile_phone = models.IntegerField(default=None)
    country = CountryField()
    instagram_account = models.CharField(max_length=100, default=None)
    youtube_account = models.CharField(max_length=100, default=None)
    website = models.URLField(default=None)
    link_company_cart = models.URLField(default=None)
    is_active = models.BooleanField(default=None)
