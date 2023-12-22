from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40, null=True)
    username = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=40, null=True)
    
    def __str__(self):
        return self.name
    
class Table(models.Model):
    table_number = models.CharField(max_length=5, null=True)
    table_capacity = models.IntegerField(null=True)
    table_status = models.CharField(max_length=12, null=True)
    
    def __str__(self):
        return self.table_number
    
class Menu(models.Model):
    menu_name = models.CharField(max_length=100, null=True)
    menu_price = models.FloatField(null=True)
    menu_description = models.TextField(null=True)
    
    def __str__(self):
        return self.menu_name

class Formula(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    directive = models.TextField(null=True)
   
    
    def __str__(self):
        return self.menu_id

class Order(models.Model):
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    order_date = models.DateField(null=True)
    grand_total = models.FloatField(null=True)
    payment_method = models.CharField(max_length=20, null=True)
    order_status = models.CharField(max_length=20, null=True)
   
    
    def __str__(self):
        return self.order_date