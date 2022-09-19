from django.db import models

# Create your models here.
class DB_tool(models.Model):
    name = models.CharField(max_length=30,default='')
    stime = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.name