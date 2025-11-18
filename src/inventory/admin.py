from django.contrib import admin
from .models import InventoryModel

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "overhaul_cost")

admin.site.register(InventoryModel,InventoryAdmin)


