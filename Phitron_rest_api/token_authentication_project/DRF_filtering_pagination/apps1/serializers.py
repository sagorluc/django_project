from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    repassword = serializers.CharField(style= {"input_type": "password"}, write_only = 'True')
    class Meta:  
        model = User
        fields = ['username', 'email', 'password', 'repassword']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    # Get data
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        repassword = self.validated_data['repassword']
        
        if password != repassword:
            raise serializers.ValidationError({'error': 'password does not matched'})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        
        account = User(username = username, email = email)
        account.set_password(password)
        account.save()
        return account
    

                    # this is for product and product reviews    
                    # =========================================

from rest_framework import serializers, viewsets
from apps1.models import Product, ProductReview

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        reviews = serializers.StringRelatedField(many= True) # dander string reader
        
        
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'