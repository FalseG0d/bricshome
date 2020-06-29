from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/profile')
    para_1=models.TextField()
    para_2=models.TextField()

    def __str__(self):
        return self.name