import uuid

from django.db import models

# Create your models here.

class EngineVariantModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    variant_name = models.CharField(max_length=255, default="")
    core_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    overhaul_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 
    top_overhaul_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 
    accessories_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 

    def __str__(self):
        return f"{self.variant_name}"


class InventoryModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    engine_variant = models.ForeignKey(EngineVariantModel, on_delete=models.PROTECT, default=None)
    project_name = models.CharField(max_length=255, default="RAE???")
    serial_number = models.CharField(max_length=255, default="NOT GIVEN")
    estimated_availability = models.DateField(default=None, null=True)
 
    def __str__(self):
        return f"{self.project_name}"

    @property
    def overhaul_cost(self):
        """All engines of a variant always have the same price"""
        return self.variant.overhaul_cost
