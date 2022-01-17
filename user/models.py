import email
from django.db import models

# Create your models here.
class Reg(models.Model):
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    con_password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_Name + ' ' + self.last_Name + ' , ' + self.email + ' , ' + str(self.phone)
