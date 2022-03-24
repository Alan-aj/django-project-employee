from django.db import models

# Create your models here.
class signup(models.Model):
    signid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
