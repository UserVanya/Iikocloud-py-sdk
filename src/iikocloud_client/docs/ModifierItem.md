# ModifierItem

Modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_image_url** | **str** | Button image URL. | [optional] 
**description** | **str** | Modifier description. | [optional] 
**id** | **str** | Modifier ID. | 
**image** | [**Image**](Image.md) | Modifier image. Replaces ButtonImageUrl. | [optional] 
**is_hidden** | **bool** | Flag indicating whether the modifier is hidden. | [optional] 
**measure_unit_type** | [**MeasureUnitType**](MeasureUnitType.md) | Unit of measurement. | [optional] 
**name** | **str** | Modifier name. | 
**restrictions** | [**Restrictions**](Restrictions.md) | Modifier selection restrictions. | [optional] 
**tags** | **List[str]** | List of tags associated with the element. | [optional] 
**weight** | **float** | Weight. | [optional] 

## Example

```python
from iikocloud_client.models.modifier_item import ModifierItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierItem from a JSON string
modifier_item_instance = ModifierItem.from_json(json)
# print the JSON string representation of the object
print(ModifierItem.to_json())

# convert the object into a dict
modifier_item_dict = modifier_item_instance.to_dict()
# create an instance of ModifierItem from a dict
modifier_item_from_dict = ModifierItem.from_dict(modifier_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


