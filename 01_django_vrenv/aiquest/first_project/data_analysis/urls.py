from django.urls import path
from . import views

urlpatterns = [
    path('ldta_a', views.data_ana, name='data')
]
