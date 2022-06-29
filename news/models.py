from django.db import models


def upload_to(instance, filename):
    return 'article_imgs/{filename}'.format(filename=filename)


class Article(models.Model):
    title= models.CharField(max_length=255)
    body= models.TextField()
    img = models.ImageField(upload_to=upload_to , blank= True ,  max_length=255) 
    date= models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=255 , default=None)
    
    def __str__(self):
        return self.title
