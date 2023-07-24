from django.urls import path
from . import views

urlpatterns = [
    path('labout_us/', views.abt_us, name='about'),
    path('teacher', views.teacher_info, name='tc'),
]
