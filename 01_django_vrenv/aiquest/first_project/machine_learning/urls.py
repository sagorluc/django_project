# import all apps
from django.urls import path
from . import views


urlpatterns = [
    path('machine/',views.machine),
    path('lrandom/',views.random),
    path('ldtree/',views.dtree),
    path('lknn/',views.knn),

]
