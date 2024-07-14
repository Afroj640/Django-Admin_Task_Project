from django.contrib import admin
from .models import CustomUser, Task

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Mobile', 'ID')
    inlines = []

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_details', 'task_type', 'user', 'answer')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)