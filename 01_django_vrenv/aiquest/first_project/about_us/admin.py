from django.contrib import admin
from about_us.models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','t_id','t_name','t_email')
    
# join with admin panel
admin.site.register(Teacher,TeacherAdmin)