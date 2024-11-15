from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import random





class Venue(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    phone = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(11)])
    email_address = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
class User(models.Model):
    first_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, null=False, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.username




class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)
    company =  models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank = True)



    def __str__(self): 
        return self.name
      
