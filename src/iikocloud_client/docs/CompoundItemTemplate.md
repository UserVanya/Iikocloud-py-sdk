# CompoundItemTemplate

Modifier scheme information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.compound_item_template import CompoundItemTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CompoundItemTemplate from a JSON string
compound_item_template_instance = CompoundItemTemplate.from_json(json)
# print the JSON string representation of the object
print(CompoundItemTemplate.to_json())

# convert the object into a dict
compound_item_template_dict = compound_item_template_instance.to_dict()
# create an instance of CompoundItemTemplate from a dict
compound_item_template_from_dict = CompoundItemTemplate.from_dict(compound_item_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


