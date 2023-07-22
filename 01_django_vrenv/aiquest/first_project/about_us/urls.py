from django.urls import path
from . import views

urlpatterns = [
    path('labout/', views.abt_us)
]
