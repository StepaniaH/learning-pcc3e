from django.db import models

class Pizza(models.Model):
    """A pizza"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topping(models.Model):
    """A topping"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    # Store the source of the topping.
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
