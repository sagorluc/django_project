from django.urls import path, include
from rest_framework import routers
from app1.views import ProductViewSet, ProductReviewViewSet

router = routers.DefaultRouter()
router.register(r'products', viewset=ProductViewSet, basename= 'product')
router.register('reviews',ProductReviewViewSet )

# create the path hare
urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls')),
]

