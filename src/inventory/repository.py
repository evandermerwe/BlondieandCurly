from inventory import models


class InventoryRepository:
    def get_all_inventory(self) -> list[models.InventoryModel]:
        all_models = models.InventoryModel.objects.all()
        return list(all_models)
