# IikoTransportPublicApiContractsMetricsCallCenterAction

Action made in Cloud Call Center.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IikoTransportPublicApiContractsMetricsActionType**](IikoTransportPublicApiContractsMetricsActionType.md) | Action type. | 
**time** | **str** | Time. | 
**duration** | **int** | Duration. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_metrics_call_center_action import IikoTransportPublicApiContractsMetricsCallCenterAction

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsMetricsCallCenterAction from a JSON string
iiko_transport_public_api_contracts_metrics_call_center_action_instance = IikoTransportPublicApiContractsMetricsCallCenterAction.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsMetricsCallCenterAction.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_metrics_call_center_action_dict = iiko_transport_public_api_contracts_metrics_call_center_action_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsMetricsCallCenterAction from a dict
iiko_transport_public_api_contracts_metrics_call_center_action_from_dict = IikoTransportPublicApiContractsMetricsCallCenterAction.from_dict(iiko_transport_public_api_contracts_metrics_call_center_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


