from django.contrib import admin
from .models import User, Agent, Lead


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login']
    ordering = ['id']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    ordering = ['id']


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age']
    ordering = ['id']
