from django.db import models # import module 

# Create your models here.
 # make table and column
 
class Teacher(models.Model):
    t_id = models.IntegerField()
    t_name = models.CharField(max_length= 50)
    t_email = models.EmailField(max_length=40)