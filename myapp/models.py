from django.db import models

# Create your models here.
# from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.

class temperature(models.Model):
    Value=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)
    comments=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class pH(models.Model):
    Value=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)
    comments=models.CharField(max_length=50)

    def __str__(self):
        return self.title