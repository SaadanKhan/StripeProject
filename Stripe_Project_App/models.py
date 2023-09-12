from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       name = models.CharField(default="", max_length=100)
       price = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)