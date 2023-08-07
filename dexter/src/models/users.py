import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Users(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.CharField(default="", max_length=200)
    password = models.CharField(default="", max_length=200)
    salt = models.CharField(default="", max_length=16)
    is_active = models.IntegerField(default=0)
    key = models.CharField(default="", max_length=35)

    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'id' # Added this line

    @property
    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Users, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'users'
        app_label = 'src'
