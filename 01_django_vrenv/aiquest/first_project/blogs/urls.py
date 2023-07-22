from django.urls import path
from . import views

urlpatterns = [
    path('lblog/', views.blog_first)
]
