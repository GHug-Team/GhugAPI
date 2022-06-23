from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name,  password, **other_fields)

    def create_user(self, email, user_name,  password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        
        if not user_name:
            raise ValueError('Users must have a username')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=False)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', ]

    def __str__(self):
        return self.email


def upload_to(instance, filename):
    return 'profile_imgs/{filename}'.format(filename=filename)



class Baby(models.Model):
    name= models.CharField(max_length=255)
    img = models.ImageField(upload_to=upload_to, blank=True, null=True,  max_length=255) 
    birthdate= models.DateField()
    weight = models.FloatField()
    height=models.FloatField()

    GENDER_CHOICES = (
        ('B', 'Boy'),
        ('G', 'Girl'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    RELATIONSHIP_CHOICES =(
        ('M','Mom'),
        ('D', 'Dad')
    )
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES)
    user= models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='baby_user')
    
    def __str__(self):
        return self.name




