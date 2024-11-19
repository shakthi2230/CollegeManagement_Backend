from django.contrib import admin
from .models import Faculty
from .forms import FacultyForm  

class FacultyAdmin(admin.ModelAdmin):

    form = FacultyForm 

    list_display = ('first_name', 'last_name', 'email', 'subject', 'phone_number')

    search_fields = ('first_name', 'last_name', 'email')

    list_filter = ('subject',)
    
    ordering = ('last_name',)

admin.site.register(Faculty, FacultyAdmin)
