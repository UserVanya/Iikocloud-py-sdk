# IikoTransportPublicApiContractsMetricsCallCenterTelemetry

Cloud Call Center actions metrics information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | Cloud Call Center operator id. | 
**actions** | [**List[IikoTransportPublicApiContractsMetricsCallCenterAction]**](IikoTransportPublicApiContractsMetricsCallCenterAction.md) |  | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_metrics_call_center_telemetry import IikoTransportPublicApiContractsMetricsCallCenterTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsMetricsCallCenterTelemetry from a JSON string
iiko_transport_public_api_contracts_metrics_call_center_telemetry_instance = IikoTransportPublicApiContractsMetricsCallCenterTelemetry.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsMetricsCallCenterTelemetry.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_metrics_call_center_telemetry_dict = iiko_transport_public_api_contracts_metrics_call_center_telemetry_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsMetricsCallCenterTelemetry from a dict
iiko_transport_public_api_contracts_metrics_call_center_telemetry_from_dict = IikoTransportPublicApiContractsMetricsCallCenterTelemetry.from_dict(iiko_transport_public_api_contracts_metrics_call_center_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


