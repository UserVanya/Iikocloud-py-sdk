# AmountUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the directory entry | [optional] 
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.amount_unit import AmountUnit

# TODO update the JSON string below
json = "{}"
# create an instance of AmountUnit from a JSON string
amount_unit_instance = AmountUnit.from_json(json)
# print the JSON string representation of the object
print(AmountUnit.to_json())

# convert the object into a dict
amount_unit_dict = amount_unit_instance.to_dict()
# create an instance of AmountUnit from a dict
amount_unit_from_dict = AmountUnit.from_dict(amount_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


