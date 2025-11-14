import typing

from django.views import generic

from inventory import repository


class InventoryView(generic.TemplateView):
    template_name = "inventory.html"

    def get_context_data(
        self, **kwargs: dict[str, typing.Any]
    ) -> dict[str, typing.Any]:
        context = super().get_context_data(**kwargs)
        inventory_repository = repository.InventoryRepository()
        context["inventory"] = inventory_repository.get_all_inventory()
        return context
