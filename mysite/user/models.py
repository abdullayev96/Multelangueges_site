from django.db import models
from django.urls import reverse

# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.base_user import AbstractBaseUser, PermissionsMixin
# from django.utils import timezone
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password, is_staff=False, is_activate=True, **extra_fields):
#         email = UserManager.normalize_email(email)
#         user= self.model(email, is_staff, is_staff, **extra_fields)
#         if password:
#             user.set_password(password)
#         user = user.save()
#         return user
#
#     def create_superuser(self, email, password, is_staff=True, is_activate=True, is_superuser=True, **extra_fields):
#         return self.create_user(email, password, is_staff, is_activate, is_superuser, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_lenght= 100, blank=False, null= False, unique =True)
#     full_name = models.Charfield(max_lenght= 200, blank=False, null=False,)
#     is_activate = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined= models.DatTimeField(default = timezone.now(), editable=False)
#
#
#     USERNAME_FIELDS = "email"
#     objects= UserManager()
#
#     def __str__(self):
#         return f"{self.email}- {self.full_name}"
#
#
# class Meta:
#     verbose_name = "user"
#     verbose_name_plural = "Users"
#     ordering = ["-date"]


class User(models.Model):
    name = models.CharField(max_length=499, verbose_name="nomi")
    title = models.TextField()
    url_name = models.URLField(max_length=400, verbose_name="Url name")
    image  = models.ImageField(upload_to='photos', verbose_name="Rasmlar")
    create_at  = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.name} || {self.title}'

    def get_absolute_url(self):
        return "/" + str(self.id) + "/"

    class Meta:
        ordering = ['-id']

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='nomi')
    subject  = models.TextField()
    number = models.PositiveIntegerField()
    tg_name =  models.CharField(max_length=200, verbose_name='telegram nomi')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}  || {self.create_at}'

    class Meta:
        ordering = ['-id']




