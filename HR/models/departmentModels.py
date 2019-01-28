from django.db import models

# Create your models here.
class Department(models.Model):
  name = models.CharField(default="", max_length=100)
  budget = models.IntegerField(default="", max_length=50)

  def __str__(self):
    return f"Name: {self.name}  Budget: {self.budget}"