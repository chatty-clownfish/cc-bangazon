from django.db import models

# Create your models here.
class Computer(models.Model):
    purchaseDate = models.CharField(max_length=200),
    decommissionDate = models.CharField(max_length= 200),
    employee = models.ManyToManyField(Employee, through= "ComputerEmployee")
    def __str__(self):
        return self.purchaseDate

#Insert into Computers ( purchaseDate, decommissionDate)
#values ("1-24-1992", "1-29-2018")