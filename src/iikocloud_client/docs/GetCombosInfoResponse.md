# GetCombosInfoResponse

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**List[WarningInfo]**](WarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 
**combo_categories** | [**List[ComboCategory]**](ComboCategory.md) | Combo&#39;s categories. | [optional] 
**combo_specifications** | [**List[ComboSpecification]**](ComboSpecification.md) | Full combo&#39;s specifications. | [optional] 

## Example

```python
from iikocloud_client.models.get_combos_info_response import GetCombosInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCombosInfoResponse from a JSON string
get_combos_info_response_instance = GetCombosInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetCombosInfoResponse.to_json())

# convert the object into a dict
get_combos_info_response_dict = get_combos_info_response_instance.to_dict()
# create an instance of GetCombosInfoResponse from a dict
get_combos_info_response_from_dict = GetCombosInfoResponse.from_dict(get_combos_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


