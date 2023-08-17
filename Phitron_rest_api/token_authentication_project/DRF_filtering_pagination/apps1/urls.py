from django.urls import path,include
from  rest_framework.authtoken.views import obtain_auth_token
from apps1.views import RegistrationView, LogoutView, ProductViewSet, ProductReviewViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', viewset=ProductViewSet, basename= 'product')
router.register('reviews',ProductReviewViewSet, basename= 'product-review' )

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # product and product reviewers
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls')),
]
