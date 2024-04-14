from django.db import models


class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
