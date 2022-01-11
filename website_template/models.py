from django.db import models

class Menu(models.Model):
    Food_name = models.CharField(max_length=100)
    Food_Catagories = models.CharField(max_length=50)
    Food_price = models.IntegerField()

    def __str__(self):
        return self.Food_name + " " +',' + " " +  self.Food_Catagories
