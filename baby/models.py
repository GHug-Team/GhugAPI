from django.db import models
from users.models import Baby, CustomUser


def upload_to(instance, filename):
    return 'album_imgs/{filename}'.format(filename=filename)
class Album(models.Model):
    title= models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to , null=True , blank= True ,  max_length=255)
    date= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_album')

    def __str__(self):
        return self.title



class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    vacc_type = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    due_date= models.DateField()
    age = models.IntegerField()
    #given_date= models.DateField()
    #baby= models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='baby_vaccines')

    
    def __str__(self):
        return self.name



