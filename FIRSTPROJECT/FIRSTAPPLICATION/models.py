from django.db import models

# Create your models here.
class FirstApp(models.Model):
    Name = models.CharField(max_length=30)
    ID=models.AutoField
    Contact = models.IntegerField
    Address = models.CharField(max_length=100)
