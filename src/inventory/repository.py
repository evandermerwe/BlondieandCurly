from inventory import models


class InventoryRepository:
    def get_all_inventory(self) -> list[models.EngineInventoryModel]:
        all_models = models.EngineInventoryModel.objects.all()
        return list(all_models)

    def get_all_engine_variants(self) -> list[models.EngineVariantModel]:
        all_models = models.EngineVariantModel.objects.all()
        return list(all_models)

    def get_engine_variant(self, variant_name: str) -> models.EngineVariantModel:
        return models.EngineVariantModel.objects.get(variant_name=variant_name)

    def get_inventory(self, serial_number: str) -> models.EngineInventoryModel:
        return models.EngineInventoryModel.objects.get(serial_number=serial_number)

    def create_inventory(self, inventory: models.EngineInventoryModel) -> None:
        inventory.save()

    def create_engine_variant(self, engine_variant: models.EngineVariantModel) -> None:
        engine_variant.save()
