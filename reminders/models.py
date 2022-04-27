from datetime import date
from django.db import models
from users.models import CustomUser


class Category(models.Model):
    title= models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    title= models.CharField(max_length=255)
    body = models.TextField()
    date= models.DateField()
    time = models.TimeField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_tasks' )
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_tasks')

    def __str__(self):
        return self.title