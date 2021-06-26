from django.db import models

# Create your models here.
from django.db.models.fields import CharField, EmailField, UUIDField
# Create your models here.
class UserModel(models.Model):
     email = EmailField(max_length = 254 , blank= True , null=True)
     status = models.BooleanField(default=False)
     def __str__(self):
         return self.email