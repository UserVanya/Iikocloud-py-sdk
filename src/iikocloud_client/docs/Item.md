# Item

Item in a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_group_ids** | **List[str]** | Allergen group IDs. | [optional] 
**combo_id** | **str** | Combo meal ID (from the Menu.combos[] array).  REQUIRED for combo meals (itemType &#x3D; \&quot;COMBO\&quot;).  NULL for regular products. | [optional] 
**description** | **str** | Item description. | [optional] 
**is_hidden** | **bool** | Flag indicating whether the item is hidden. | [optional] 
**item_type** | **str** | Item type: \&quot;PRODUCT\&quot; (default), \&quot;COMBO\&quot;.  If not set (null), treated as PRODUCT for backward compatibility with the old menu schema. | [optional] 
**labels** | **List[str]** | List of website tags associated with the item. | [optional] 
**modifier_groups** | [**List[ModifierGroup]**](ModifierGroup.md) | Modifier groups. | [optional] 
**name** | **str** | Item name. | 
**product_id** | **str** | Product ID.  REQUIRED for regular products (itemType &#x3D; null or \&quot;PRODUCT\&quot;).  NULL for combo meals (itemType &#x3D; \&quot;COMBO\&quot;). | [optional] 
**size_prices** | [**List[MenuV3SizePrice]**](MenuV3SizePrice.md) | Prices by size. | [optional] 
**sizes** | [**List[ComboSize]**](ComboSize.md) | Combo sizes with visual information (images, visibility).  Used only when itemType &#x3D; \&quot;COMBO\&quot;.  Ignored for PRODUCT (sizePrices[] is used instead).  Contains information specific to placement in a group. | [optional] 
**sort_order** | **float** | Sort order of the item in a group (starting from 0).  Optional — for explicit sorting in the UI. | [optional] 
**tags** | **List[str]** | List of internal tags associated with the item. | [optional] 

## Example

```python
from iikocloud_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


