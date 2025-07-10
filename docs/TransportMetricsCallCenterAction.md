# TransportMetricsCallCenterAction

Action made in Cloud Call Center.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransportMetricsActionType**](TransportMetricsActionType.md) | Action type. | 
**time** | **str** | Time. | 
**duration** | **int** | Duration. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_metrics_call_center_action import TransportMetricsCallCenterAction

# TODO update the JSON string below
json = "{}"
# create an instance of TransportMetricsCallCenterAction from a JSON string
transport_metrics_call_center_action_instance = TransportMetricsCallCenterAction.from_json(json)
# print the JSON string representation of the object
print(TransportMetricsCallCenterAction.to_json())

# convert the object into a dict
transport_metrics_call_center_action_dict = transport_metrics_call_center_action_instance.to_dict()
# create an instance of TransportMetricsCallCenterAction from a dict
transport_metrics_call_center_action_from_dict = TransportMetricsCallCenterAction.from_dict(transport_metrics_call_center_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


