# CallCenterAction

Action made in Cloud Call Center.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Duration. | [optional] 
**time** | **str** | Time. | 
**type** | [**ActionType**](ActionType.md) | Action type. | 

## Example

```python
from iikocloud_client.models.call_center_action import CallCenterAction

# TODO update the JSON string below
json = "{}"
# create an instance of CallCenterAction from a JSON string
call_center_action_instance = CallCenterAction.from_json(json)
# print the JSON string representation of the object
print(CallCenterAction.to_json())

# convert the object into a dict
call_center_action_dict = call_center_action_instance.to_dict()
# create an instance of CallCenterAction from a dict
call_center_action_from_dict = CallCenterAction.from_dict(call_center_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


