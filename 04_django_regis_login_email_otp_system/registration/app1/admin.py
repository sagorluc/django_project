from django.contrib import admin
from .models import NameModel
from .forms import HomeForm

# Register your models here.
admin.site.register(NameModel) # join with database admin panel