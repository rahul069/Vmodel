from django.db import models



from django.db import models

class ModelUsers(models.Model):
   # id      = models.CharField(max_length=50,unique=True)
    name    = models.CharField(max_length=50)
    email    = models.EmailField(max_length=70,blank=True,primary_key=True)
    password = models.CharField(max_length=50)
    isActive  = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title