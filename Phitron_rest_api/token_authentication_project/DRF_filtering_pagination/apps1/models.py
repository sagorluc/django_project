from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 40)
    description = models.TextField()
    price = models.DecimalField(max_digits= 10, decimal_places= 2)
    
    
    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'reviews')
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    rating = models.IntegerField(choices=[(i, i)for i in range(1,6)])
    review = models.TextField()
    create_at = models.DateTimeField(auto_now_add= True) # object jokhone create hoice sei start time save hobe
    update_at = models.DateTimeField(auto_now= True) # jokhn edit korbe sei time update hobe
    
    class Meta:
        unique_together = ('product', 'user') # ekta product er under e ektai review korte parbe ek jon user.
                                              # multipale review korte parbe nah ek jon user ekti product e.
                                              
    def __str__(self) :
        return f"{self.user.username} {self.product.name} Rating: {self.rating}"
    
