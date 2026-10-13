# ModifierItem

Modifier item in a group.  All fields except Id are optional overrides: when a field is null,  its value must be taken from the reference Modifier (MenuV3.modifiers) with the same Id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_image_url** | **str** | Button image URL.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**description** | **str** | Modifier description.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**id** | **str** | Modifier ID. | 
**image** | [**Image**](Image.md) | Modifier image. Replaces ButtonImageUrl.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**is_hidden** | **bool** | Flag indicating whether the modifier is hidden.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**measure_unit_type** | [**MeasureUnitType**](MeasureUnitType.md) | Unit of measurement.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**name** | **str** | Modifier name.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**restrictions** | [**Restrictions**](Restrictions.md) | Modifier selection restrictions.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**tags** | **List[str]** | List of tags associated with the element.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 
**weight** | **float** | Weight.  If null, the value is taken from the reference Modifier with the same Id. | [optional] 

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


