from django.db import models
from django.urls import reverse

class ComputerEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, )
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, )