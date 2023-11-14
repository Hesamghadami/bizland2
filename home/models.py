from django.db import models
import datetime

class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio',default='portfolio.jpg')
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    project_date = models.DateTimeField(default=datetime.datetime.now())
    project_url =  models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title1
    
class Comment (models.Model):
    image = models.ImageField(upload_to='comment',default='comment.jpg')
    info = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    comment = models.TextField()
    def __str__(self):
        return self.info.username

    
class Teammember(models.Model):
    image = models.ImageField(upload_to='portfolio',default='portfolio.jpg')
    info = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    twitter = models.CharField(max_length=255,default='#')
    facebook = models.CharField(max_length=255,default='#')
    instagram = models.CharField(max_length=255,default='#')
    linkdin = models.CharField(max_length=255,default='#')
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username
    
class Price(models.Model):
    title = models.CharField(max_length=255)
    fee = models.CharField(max_length=20)
    content1= models.TextField()
    content2= models.TextField()
    content3= models.TextField()
    content4= models.TextField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
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