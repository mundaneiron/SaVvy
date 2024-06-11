from django.db import models

# Create your models here.

class Userdetails(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirmPassword= models.CharField(max_length=20)

    class Meta:
        db_table = "userdetails"