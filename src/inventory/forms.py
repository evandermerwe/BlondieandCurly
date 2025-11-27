from django import forms
from .models import EngineVariantModel

# class VariantCostUpdateForm(forms.ModelForm):
#     class Meta:
#         model = EngineVariantModel
#         fields = ['overhaul_cost']
#         widgets = {
#             'overhaul_cost': forms.NumberInput(attrs={
#                 'step': '50.00',
#                 'class': 'form-control',
#                 'placeholder': 'e.g. 45999.99'
#             })
#         }
#         labels = {
#             'overhaul_cost': 'New Price for All Engines of This Variant'
#         }
