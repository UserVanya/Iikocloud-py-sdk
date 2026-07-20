# SimpleModifierInfo

Modifier details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_amount** | **int** | Default quantity. | [optional] 
**free_of_charge_amount** | **int** | Free of charge amount. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**hide_if_default_amount** | **bool** | Hide if default amount applied. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**id** | **UUID** | ID. | 
**max_amount** | **int** | Maximum quantity. | 
**min_amount** | **int** | Minimum quantity. | 
**required** | **bool** | Required availability. | [optional] 
**splittable** | **bool** | Modifier can be split. This field is supported since 7.2.4 iikoRMS version. | [optional] 

## Example

```python
from iikocloud_client.models.simple_modifier_info import SimpleModifierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleModifierInfo from a JSON string
simple_modifier_info_instance = SimpleModifierInfo.from_json(json)
# print the JSON string representation of the object
print(SimpleModifierInfo.to_json())

# convert the object into a dict
simple_modifier_info_dict = simple_modifier_info_instance.to_dict()
# create an instance of SimpleModifierInfo from a dict
simple_modifier_info_from_dict = SimpleModifierInfo.from_dict(simple_modifier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


