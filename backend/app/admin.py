from django.contrib import admin
from .models import Contact, Registration

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'course', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['full_name', 'email']
