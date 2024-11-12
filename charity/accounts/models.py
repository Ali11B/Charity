from django.db import models

class Benefactor (models.Model):
    experience = models.SmallIntegerField(default=0)

class Charity (models.Moedel):
    name = models.CharField(max_length=50)



class Task (models.Moodel):
    assigned_benefactor = models.ForeignKey(Benefactor , on_delete= models.SET_NULL)
    charity = models.ForeignKey(Charity,on_delete=models.CASCADE)
    age_limit_from = models.IntegerField()
    age_limit_to = models.IntegerField()

