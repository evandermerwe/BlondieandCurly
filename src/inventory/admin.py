from django.contrib import admin
from .models import EngineInventoryModel, EngineVariantModel

# Register your models here.
class EngineVariantAdmin(admin.ModelAdmin[EngineVariantModel]):
    list_display = ("variant_name", "overhaul_cost")


class EngineInventoryAdmin(admin.ModelAdmin[EngineInventoryModel]):
    list_display = ("engine_variant", "serial_number", "project_name")

admin.site.register(EngineVariantModel,EngineVariantAdmin)
admin.site.register(EngineInventoryModel,EngineInventoryAdmin)



