from django.urls import path
from . import views

urlpatterns = [
    path('ldta_a/', views.data_ana, name='data'),
    path('view/', views.Data_Analysis.as_view(), name='class_base'),
]
