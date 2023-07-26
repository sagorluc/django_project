from django.urls import path
from . import views

urlpatterns = [
    path('ldpl/', views.dp_learning),
    path('lauth/', views.author_registration),
]
