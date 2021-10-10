from django.db import models
from django.urls import reverse

# Create your models here.

class Owner(models.Model):
    owner_name = models.CharField(max_length=100, default="Adebayo Car", null=True)     
    def __str__(self):
        return self.owner_name


class Car(models.Model):
    name = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200 )
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

