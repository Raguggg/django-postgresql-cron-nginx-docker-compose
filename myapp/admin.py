from django.contrib import admin
from .models import MyModel
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    
admin.site.register(MyModel, MyModelAdmin)