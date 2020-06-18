from django.db import models
import datetime

# Create your models here.
class Slider(models.Model):
    image=models.ImageField(upload_to='images/slider')
    name=models.CharField(max_length=20)
    first=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Report(models.Model):
    thumbnail=models.ImageField(upload_to='reports/thumbnails')
    image=models.ImageField(upload_to='reports/images')
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    abstract=models.TextField()
    complete=models.TextField()
    pdf=models.FileField(upload_to='reports/file')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class About(models.Model):
    logo=models.ImageField(upload_to='images')
    name=models.CharField(max_length=100)
    map_snippet=models.CharField(max_length=500)
    about=models.TextField()
    about_abstract=models.TextField()
    history=models.TextField()
    history_abstract=models.TextField()
    email=models.EmailField()
    password=models.CharField(max_length=50)
    number=models.CharField(max_length=20)


    def __str__(self):
        return self.name

class Video(models.Model):
    source_url=models.CharField(max_length=300)
    video_content=models.TextField()

class GalleryImage(models.Model):
    image=models.ImageField(upload_to='images/recent')
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Event(models.Model):
    image=models.ImageField(upload_to='images/recent')
    name=models.CharField(max_length=20)
    description=models.TextField()
    time = models.DateTimeField(auto_now=True)
    venue=models.CharField(max_length=500)


    def __str__(self):
        return self.name

class Link(models.Model):
    name=models.CharField(max_length=20)
    
    ICON=(
        ('fa fa-facebook','Facebook'),
        ('fa fa-instagram','Instagram'),
        ('fa fa-twitter','Twitter'),
        ('fa fa-linkedin','LinkedIn'),
        ('fa fa-pintrest','Pintrest'),
        ('fa fa-snapchat','Snapchat'),
        ('fa fa-youtube','Youtube'),
        ('fa fa-reddit-alien','Reddit'),
        ('fa fa-medium','Medium'),
        ('fa fa-google-plus','Google Plus'),
        ('fa fa-js-fiddle','Fiddle'),
        ('fa fa-github','Github'),
    )
    icon=models.CharField(max_length=120,choices=ICON,default=ICON[0][0])
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.name