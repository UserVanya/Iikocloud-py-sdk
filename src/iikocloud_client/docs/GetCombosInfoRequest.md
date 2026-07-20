# GetCombosInfoRequest

Get combos info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_data** | **bool** | Extra data. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.get_combos_info_request import GetCombosInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCombosInfoRequest from a JSON string
get_combos_info_request_instance = GetCombosInfoRequest.from_json(json)
# print the JSON string representation of the object
print(GetCombosInfoRequest.to_json())

# convert the object into a dict
get_combos_info_request_dict = get_combos_info_request_instance.to_dict()
# create an instance of GetCombosInfoRequest from a dict
get_combos_info_request_from_dict = GetCombosInfoRequest.from_dict(get_combos_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


