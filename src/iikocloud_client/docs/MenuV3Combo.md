# MenuV3Combo

Combo meal.  Consists of component groups, each group offers a choice of products.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_groups** | [**List[ComboComponentGroup]**](ComboComponentGroup.md) | Combo component groups (Burger, Drink, Fries, etc.). | 
**id** | **UUID** | Unique combo ID.  Unique within the combos[] array — each combo appears only once. | 
**labels** | **List[str]** | List of website tags. | [optional] 
**price_strategy** | [**PriceStrategy**](PriceStrategy.md) | Pricing strategy.  BY_COMPONENT (default): price is composed from selected components.  FIXED: fixed combo price. | [optional] 
**sku** | **str** | Combo SKU. | 
**tags** | **List[str]** | List of internal tags. | [optional] 

## Example

```python
from iikocloud_client.models.menu_v3_combo import MenuV3Combo

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3Combo from a JSON string
menu_v3_combo_instance = MenuV3Combo.from_json(json)
# print the JSON string representation of the object
print(MenuV3Combo.to_json())

# convert the object into a dict
menu_v3_combo_dict = menu_v3_combo_instance.to_dict()
# create an instance of MenuV3Combo from a dict
menu_v3_combo_from_dict = MenuV3Combo.from_dict(menu_v3_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


