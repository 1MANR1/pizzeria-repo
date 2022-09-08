from django.db import models

class Pizza(models.Model):
    """pizza name"""
    name = models.CharField(max_length=200)
    #date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Topping(models.Model):
    """pizza toppings"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    #date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    