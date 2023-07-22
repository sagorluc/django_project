"""
URL configuration for aiquest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import all apps
from django.contrib import admin
from django.urls import path
from machine_learning.views import machine
from machine_learning.views import deep_learning
from machine_learning.views import about_us
from blogs import views as b
from deep_learning import views as dpl
from data_analysis import views as dta
from about_us import views as abt_us

# connect path with main url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('machine_learning/',machine),
    path('dl/',deep_learning),
    path('about/',about_us),
    path('blog/', b.blog_first),
    path('dpl/', dpl.dp_learning),
    path('dta/', dta.data_ana),
    path('abt/',abt_us.abt_us)
]

