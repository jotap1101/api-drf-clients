from client.models import Client
from django.contrib import admin

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['name', 'rg', 'cpf', 'birth_date', 'email', 'phone', 'status']
    list_display_links = ['name']
    list_editable = ['status']
    list_filter = ['status']
    list_per_page = 10
    search_fields = ['name', 'rg', 'cpf', 'email', 'phone']
    ordering = ['name']

admin.site.register(Client, ClientAdmin)