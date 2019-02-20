from django.db import models

# Create your models here.
# dog functions
class Dogs(models.Model):
    dog_name = models.CharField(max_length=300)
    dog_color = models.CharField(max_length=300)
    dog_breed = models.CharField(max_length=300)
    dog_gender = models.CharField(max_length= 300)

# account functions
class Account(models.Model):
    username = models.CharField(max_length=300)
    realname = models.CharField(max_length=300)
    accountnumber = models.CharField(max_length=300)
    balance = models.IntegerField()
