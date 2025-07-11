# TransportEmployeesActiveCourierLocation

Courier's location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_id** | **str** | Employee ID. | [optional] 
**last_active_latitude** | **float** | Latitude. | [optional] 
**last_active_longitude** | **float** | Longitude. | [optional] 
**last_active_client_date** | **str** | Client date and time. | [optional] 

## Example

```python
from iikocloud_client.models.transport_employees_active_courier_location import TransportEmployeesActiveCourierLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesActiveCourierLocation from a JSON string
transport_employees_active_courier_location_instance = TransportEmployeesActiveCourierLocation.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesActiveCourierLocation.to_json())

# convert the object into a dict
transport_employees_active_courier_location_dict = transport_employees_active_courier_location_instance.to_dict()
# create an instance of TransportEmployeesActiveCourierLocation from a dict
transport_employees_active_courier_location_from_dict = TransportEmployeesActiveCourierLocation.from_dict(transport_employees_active_courier_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


