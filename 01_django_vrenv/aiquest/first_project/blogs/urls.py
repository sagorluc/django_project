from django.urls import path
from . import views

urlpatterns = [
    path('lblog/', views.blog_first),
    path('lform/', views.show_forms_data, name='form'),
]
