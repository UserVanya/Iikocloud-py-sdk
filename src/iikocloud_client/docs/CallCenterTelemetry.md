# CallCenterTelemetry

Cloud Call Center actions metrics information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[CallCenterAction]**](CallCenterAction.md) |  | 
**employee_id** | **UUID** | Cloud Call Center operator id. | 

## Example

```python
from iikocloud_client.models.call_center_telemetry import CallCenterTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of CallCenterTelemetry from a JSON string
call_center_telemetry_instance = CallCenterTelemetry.from_json(json)
# print the JSON string representation of the object
print(CallCenterTelemetry.to_json())

# convert the object into a dict
call_center_telemetry_dict = call_center_telemetry_instance.to_dict()
# create an instance of CallCenterTelemetry from a dict
call_center_telemetry_from_dict = CallCenterTelemetry.from_dict(call_center_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


