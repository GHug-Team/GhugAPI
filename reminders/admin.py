from asyncio import tasks
from unicodedata import category
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Task

admin.site.register(Category)
admin.site.register(Task)