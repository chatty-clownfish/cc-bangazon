from django.db import models
from django.urls import reverse

class Training(models.Model):
  name = models.CharField(default="", max_length=100)
  start_date = models.CharField(default="", max_length=100)
  end_date = models.CharField(default="", max_length=100)
  maxAttendees = models.CharField(default="", max_length=100)
  employees = models.ManyToManyField(Employee, through='EmployeeTraining')

  def __str__(self):
    return self.name
