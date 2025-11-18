import uuid

from django.db import models

# Create your models here.


class InventoryModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    core_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    overhaul_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 
    top_overhaul_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 
    accessories_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 

    def __str__(self):
        return f"{self.name}"
