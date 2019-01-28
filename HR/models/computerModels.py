from django.db import models

# Create your models here.
class Computers(models.Model):
    purchaseDate = models.CharField(max_length=200),
    decommissionDate = models.CharField(max_length= 200),

    def __str__(self):
        return self.purchaseDate

#insert into Album ( purchaseDate, decommissionDate)
#values ("1-24-1992", "1-29-2018")  