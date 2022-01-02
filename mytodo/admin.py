from django.contrib import admin
from .models import MyTodo
# Register your models here.

# admin.site.register(MyTodo)

@admin.register(MyTodo)
class MyTodoAdmin(admin.ModelAdmin):
    list_display = ['title','complete','created_at']
    list_filter=['complete','created_at']
    readonly_fields = ['created_at']