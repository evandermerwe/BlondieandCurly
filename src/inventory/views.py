import typing
from django.views import generic
from inventory import repository

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db import transaction
from .models import EngineVariantModel
# from .forms import VariantCostUpdateForm

class InventoryView(generic.TemplateView):
    template_name = "inventory.html"

    def get_context_data(
        self, **kwargs: dict[str, typing.Any]
    ) -> dict[str, typing.Any]:
        context = super().get_context_data(**kwargs)
        inventory_repository = repository.InventoryRepository()
        context["inventory"] = inventory_repository.get_all_inventory()
        return context


# @login_required
# def variant_list(request):
#     variants = EngineVariantModel.objects.annotate(
#         engine_count=models.Count('engines')
#     ).order_by('name')
#     return render(request, 'engines/variant_list.html', {
#         'variants': variants
#     })
#
# @login_required
# def update_variant_price(request, variant_id):
#     variant = get_object_or_404(EngineVariant, id=variant_id)
#     engine_count = variant.engines.filter(is_active=True).count()
#
#     if request.method == 'POST':
#         form = VariantPriceUpdateForm(request.POST, instance=variant)
#         if form.is_valid():
#             with transaction.atomic():
#                 form.save()
#             messages.success(
#                 request,
#                 f"Price updated! All {engine_count} active engine(s) "
#                 f"of '{variant.name}' now cost ${variant.base_price:,}."
#             )
#             return redirect('variant_list')
#     else:
#         form = VariantPriceUpdateForm(instance=variant)
#
#     return render(request, 'engines/update_price.html', {
#         'form': form,
#         'variant': variant,
#         'engine_count': engine_count,
#     })
