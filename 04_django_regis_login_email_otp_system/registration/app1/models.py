from django.db import models

# Create your models here.
class NameModel(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 40)
    from_email = models.EmailField(max_length= 40)
    message = models.TextField()
