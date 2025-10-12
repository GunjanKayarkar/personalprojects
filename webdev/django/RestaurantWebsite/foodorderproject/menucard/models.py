from django.db import models

# Create your models here.

class Menu(models.Model):
    dish_number = models.IntegerField()
    dish_name = models.CharField(max_length=100)
    #dish_price = models.IntegerField()

    def __str__(self):
        return self.dish_name


class Orderid(models.Model):
    STATUS = (
        ('Progressing', 'Progressing'),
        ('Prepared', 'Prepared'),
        ('Completed', 'Completed'),
    )

    ordernumber = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    #total = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now_add=True)
    fooditem = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    order_status = models.CharField(max_length=100, choices=STATUS, default='Progressing')

    def __str__(self):
        return self.name

