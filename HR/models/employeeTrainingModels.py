from django.db import models
from django.urls import reverse

class EmployeeTraining(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, )
    training = models.ForeignKey(Training, on_delete=models.CASCADE, )
