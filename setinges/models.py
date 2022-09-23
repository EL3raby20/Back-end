from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=40)
    logo=models.ImageField(upload_to="Company/")
    call_us=models.CharField(max_length=40)
    email_us=models.EmailField()
    subtaitl=models.TextField(max_length=500)
    fb_link=models.URLField(null=True,blank=True)
    insta_link=models.URLField(null=True,blank=True)
    twiter=models.URLField(null=True,blank=True)
    email=models.TextField(max_length=100)
    numbers=models.TextField(max_length=100)
    address=models.TextField(max_length=100)

    def __str__ (self):
        return self.name
