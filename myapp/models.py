from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default=1)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=200)

    def __str__(self):
      return self.name
    
