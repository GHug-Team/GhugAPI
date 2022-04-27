from django.db import models


class Article(models.Model):
    title= models.CharField(max_length=255)
    body= models.TextField()
    img = models.ImageField(upload_to='imgs/%Y/%m/%d/' , blank= True ,  max_length=255) 
    date= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
