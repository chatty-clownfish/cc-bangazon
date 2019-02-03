from django.db import models
from django.urls import reverse


'''
Daniel Combs
[Joint table in the database connectign employees with their Training programs]
'''

class EmployeeTraining(models.Model):
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, )
    training = models.ForeignKey("Training", on_delete=models.CASCADE, )
