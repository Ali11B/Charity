from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser) : 
    Gender_LOV = (('F','F') , ('M' , 'M'))
    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True , null= True)
    description = models.TextField(blank=True , null = True)
    gender = models.CharField(max_length= 1 , blank= True , null =True , choices= Gender_LOV)
    phone = models.CharField(max_length= 15 , blank= True , null= True)