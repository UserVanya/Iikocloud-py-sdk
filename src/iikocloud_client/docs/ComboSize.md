# ComboSize

Combo size with visualization info.  Used in Item.sizes[] for COMBO elements.  Contains data specific to placement in a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_image_url** | **str** | Button image URL. | [optional] 
**image** | [**Image**](Image.md) | Combo size image (placement-specific). Replaces ButtonImageUrl. | [optional] 
**is_hidden** | **bool** | Whether this size is hidden. | [optional] 
**name** | **str** | Size name. IMPORTANT: may be an empty string \&quot;\&quot; — this is a valid value. | 
**short_name** | **str** | Short name (e.g. \&quot;L\&quot;). | [optional] 
**size_id** | **UUID** | Combo size ID.  Corresponds to product size IDs (Product.sizePrices[].sizeId). | 

## Example

```python
from iikocloud_client.models.combo_size import ComboSize

# TODO update the JSON string below
json = "{}"
# create an instance of ComboSize from a JSON string
combo_size_instance = ComboSize.from_json(json)
# print the JSON string representation of the object
print(ComboSize.to_json())

# convert the object into a dict
combo_size_dict = combo_size_instance.to_dict()
# create an instance of ComboSize from a dict
combo_size_from_dict = ComboSize.from_dict(combo_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


