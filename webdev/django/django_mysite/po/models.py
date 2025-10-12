from django.db import models

# Create your models here.
class Regist(models.Model):
    
    email = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True , null= True)
    password = models.CharField(max_length=256, blank=True , null=True)
    
    class Meta:
        db_table='Regist'

        