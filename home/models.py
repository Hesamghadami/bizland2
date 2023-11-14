from django.db import models
import datetime
  
class NewsLetter (models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name