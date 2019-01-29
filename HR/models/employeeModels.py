from django.db import models
import datetime

class Employee(models.Model):
  first_name = models.CharField(default="", max_length=100)
  last_name = models.CharField(default="", max_length=100)
  department = models.ForeignKey("Department", on_delete=models.CASCADE,)
  start_date = models.DateField(blank=True, null=True)
  is_supervisor = models.BooleanField(default=False)

  def __str__(self):
    return f"First Name: {self.first_name} Last Name: {self.last_name}"