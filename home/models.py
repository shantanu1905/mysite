from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
    msg=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Project(models.Model):
    pname=models.CharField(max_length=100)
    startdate=models.DateField()
    enddate=models.DateField()
    description=models.TextField(max_length=500)
    url=models.TextField(max_length=100)

    def __str__(self):
        return self.pname
    
    


    

  