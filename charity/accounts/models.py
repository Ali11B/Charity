from django.db import models

class Benefactor (models.Model):
    experience = models.SmallIntegerField(default=0)

class Charity (models.Moedel):
    name = models.CharField(max_length=50)



class Task (models.Moodel):
    state_LOV = (
                    ('P' , 'Pending'),
                    ('W' , 'Waiting'),
                    ('A' , 'Assigned'),
                    ('D' , 'Done') )
    gender_LOV = (
        ('F','F'),
        ('M' , 'M')
    )
    
    assigned_benefactor = models.ForeignKey(Benefactor , on_delete= models.SET_NULL)
    charity = models.ForeignKey(Charity)
    age_limit_from = models.IntegerField()
    age_limit_to = models.IntegerField()
    date = models.DateField()
    state = models.CharField(max_length=10 , choices=state_LOV)
    title = models.CharField(max_length= 60)
    gender_limit = models.CharField(max_length=1 , choices= gender_LOV)