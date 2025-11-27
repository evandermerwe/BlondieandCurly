from django.contrib import admin
from .models import InventoryModel, EngineVariantModel

# Register your models here.
class EngineVariantAdmin(admin.ModelAdmin):
    list_display = ("variant_name", "overhaul_cost")


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("engine_variant", "serial_number", "project_name")

admin.site.register(EngineVariantModel,EngineVariantAdmin)
admin.site.register(InventoryModel,InventoryAdmin)



