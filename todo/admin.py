from django.contrib import admin
from .models import Task

# Register your models here. Admin Panels me dikhne ke liye ye karna zaruri hai isse "is_completed", "updated_at" bhi dikhne lagega admin panel me
class TaskAdmin(admin.ModelAdmin):
    # ye saari fields admin panel me dikhne lagega..
    list_display = ('task', 'is_completed', 'updated_at')

    search_fields = ('task',)  # search box me task ke naam se search karne ke liye ye karna zaruri hai..

admin.site.register(Task, TaskAdmin)