from django.db import models
from .employeeModels import Employee



class Computer(models.Model):
    purchaseDate = models.CharField(max_length=200)
    decommissionDate = models.CharField(max_length=200)
    employee = models.ManyToManyField("Employee", through="ComputerEmployee")

    def __str__(self):
        return self.purchaseDate