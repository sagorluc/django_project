from django.shortcuts import render
from rest_framework import viewsets
from app1.serializes import ProductSerializer, ProductReviewSerializer
from app1.models import Product, ProductReview
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from app1.permisions import AdminOrReadOnly, ReviewerOrReadOnly

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] # giving permision.without authentication can't see the product.can see only review
    # permission_classes = [IsAuthenticatedOrReadOnly] # giving permision.without authentication see the product.can see only review and can't edit
    permission_classes = [AdminOrReadOnly] # custom permission
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # convert to json format
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [ReviewerOrReadOnly] # custom permission
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer # convert to json format
    