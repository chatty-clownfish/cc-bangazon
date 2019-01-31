from django.db import models

# model used to construct Departments

class Department(models.Model):
  # departments have two properties, name and budget
  name = models.CharField(default="", max_length=100)
  # budget must be a number
  budget = models.IntegerField()

  def __str__(self):
    return f"Name: {self.name}  Budget: {self.budget}"
