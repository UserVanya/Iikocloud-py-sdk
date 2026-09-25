import pytest


@pytest.mark.parametrize("restrictions", [{"defaultQuantity": 0, "maxQuantity": 1}, None])
def test_modifier_group_restrictions_decode_to_the_single_reviewed_model(
    restrictions: dict[str, int] | None,
) -> None:
    from iikocloud_client.models.external_menu_modifier_group import ExternalMenuModifierGroup
    from iikocloud_client.models.external_menu_modifier_group2 import (
        ExternalMenuModifierGroup2,
    )
    from iikocloud_client.models.modifier_restrictions_dto import ModifierRestrictionsDto
    from iikocloud_client.models.modifier_restrictions_dto2 import ModifierRestrictionsDto2

    v2_group = ExternalMenuModifierGroup.from_dict({"items": [], "restrictions": restrictions})
    v3_group = ExternalMenuModifierGroup2.from_dict(
        {"items": [], "splittable": False, "restrictions": restrictions}
    )

    if restrictions is None:
        assert v2_group.restrictions is None
        assert v3_group.restrictions is None
    else:
        assert type(v2_group.restrictions) is ModifierRestrictionsDto
        assert type(v3_group.restrictions) is ModifierRestrictionsDto2
        assert v2_group.restrictions.max_quantity == 1
        assert v3_group.restrictions.max_quantity == 1
