# MetricsCallCenterAction

Action made in Cloud Call Center.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MetricsActionType**](MetricsActionType.md) | Action type. | 
**time** | **str** | Time. | 
**duration** | **int** | Duration. | [optional] 

## Example

```python
from iikocloud_client.models.metrics_call_center_action import MetricsCallCenterAction

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsCallCenterAction from a JSON string
metrics_call_center_action_instance = MetricsCallCenterAction.from_json(json)
# print the JSON string representation of the object
print(MetricsCallCenterAction.to_json())

# convert the object into a dict
metrics_call_center_action_dict = metrics_call_center_action_instance.to_dict()
# create an instance of MetricsCallCenterAction from a dict
metrics_call_center_action_from_dict = MetricsCallCenterAction.from_dict(metrics_call_center_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


