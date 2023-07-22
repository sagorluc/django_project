from django.urls import path
from . import views

urlpatterns = [
    path('ldta', views.data_ana)
]
