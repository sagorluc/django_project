from rest_framework import serializers, viewsets
from app1.models import Product, ProductReview

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        reviews = serializers.StringRelatedField(many= True) # dander string reader
        
        
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'