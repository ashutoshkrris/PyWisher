from django.db import models

# Create your models here.
class Person(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    email = models.EmailField()
    bday = models.DateField()
    year = models.IntegerField()

    def __str__(self):
        return self.receiver
