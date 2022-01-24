from django.db import models
import email

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,null=True, blank=True)
    username = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=30)
    con_password = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return self.first_name
