from django.db import models
from users.models import Baby, CustomUser

class Album(models.Model):
    title= models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/' , blank= True ,  max_length=255)
    date= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_album')


class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    vacc_type = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    due_date= models.DateField()
    age = models.IntegerField()
    #given_date= models.DateField()
    #baby= models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='baby_vaccines')


