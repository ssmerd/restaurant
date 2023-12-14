from django.db import models

# Create your models here.

class BookTable(models.Model):
    """ BookTable model """

    name = models.CharField(max_length=50, blank=False)

    email =models.EmailField(blank=False)

    phone = models.CharField(max_length=20, blank=False)
    
    date = models.DateField(blank=False)

    time = models.TimeField(blank=False)
    
    no_of_people = models.IntegerField(blank=False)
    
    message = models.CharField(max_length=250, blank=True)


class Table(models.Model):
    pass
