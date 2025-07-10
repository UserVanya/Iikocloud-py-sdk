# TransportMetricsCallCenterTelemetry

Cloud Call Center actions metrics information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Cloud Call Center operator id. | 
**actions** | [**List[TransportMetricsCallCenterAction]**](TransportMetricsCallCenterAction.md) |  | 

## Example

```python
from iiko_cloud_client.models.transport_metrics_call_center_telemetry import TransportMetricsCallCenterTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of TransportMetricsCallCenterTelemetry from a JSON string
transport_metrics_call_center_telemetry_instance = TransportMetricsCallCenterTelemetry.from_json(json)
# print the JSON string representation of the object
print(TransportMetricsCallCenterTelemetry.to_json())

# convert the object into a dict
transport_metrics_call_center_telemetry_dict = transport_metrics_call_center_telemetry_instance.to_dict()
# create an instance of TransportMetricsCallCenterTelemetry from a dict
transport_metrics_call_center_telemetry_from_dict = TransportMetricsCallCenterTelemetry.from_dict(transport_metrics_call_center_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


