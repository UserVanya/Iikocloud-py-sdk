# GetManualConditionsResponse

Get manual conditions response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_conditions** | [**List[ManualConditionInfo]**](ManualConditionInfo.md) | Info about manual conditions. | [optional] 

## Example

```python
from iikocloud_client.models.get_manual_conditions_response import GetManualConditionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetManualConditionsResponse from a JSON string
get_manual_conditions_response_instance = GetManualConditionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetManualConditionsResponse.to_json())

# convert the object into a dict
get_manual_conditions_response_dict = get_manual_conditions_response_instance.to_dict()
# create an instance of GetManualConditionsResponse from a dict
get_manual_conditions_response_from_dict = GetManualConditionsResponse.from_dict(get_manual_conditions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


