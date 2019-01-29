from django.db import models
from django.urls import reverse

class Training(models.Model):
  name = models.CharField(default="", max_length=100)
  start_date = models.DateField()
  end_date = models.DateField()
  maxAttendees = models.IntegerField()
  employees = models.ManyToManyField(Employee, through='EmployeeTraining')

  def __str__(self):
    return self.name
