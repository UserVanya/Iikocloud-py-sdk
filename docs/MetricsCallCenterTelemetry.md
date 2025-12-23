# MetricsCallCenterTelemetry

Cloud Call Center actions metrics information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Cloud Call Center operator id. | 
**actions** | [**List[MetricsCallCenterAction]**](MetricsCallCenterAction.md) |  | 

## Example

```python
from iikocloud_client.models.metrics_call_center_telemetry import MetricsCallCenterTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsCallCenterTelemetry from a JSON string
metrics_call_center_telemetry_instance = MetricsCallCenterTelemetry.from_json(json)
# print the JSON string representation of the object
print(MetricsCallCenterTelemetry.to_json())

# convert the object into a dict
metrics_call_center_telemetry_dict = metrics_call_center_telemetry_instance.to_dict()
# create an instance of MetricsCallCenterTelemetry from a dict
metrics_call_center_telemetry_from_dict = MetricsCallCenterTelemetry.from_dict(metrics_call_center_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


