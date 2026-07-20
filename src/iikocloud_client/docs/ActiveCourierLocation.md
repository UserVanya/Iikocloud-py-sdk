# ActiveCourierLocation

Courier's location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_id** | **UUID** | Employee ID. | [optional] 
**last_active_client_date** | **str** | Client date and time. | [optional] 
**last_active_latitude** | **float** | Latitude. | [optional] 
**last_active_longitude** | **float** | Longitude. | [optional] 

## Example

```python
from iikocloud_client.models.active_courier_location import ActiveCourierLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveCourierLocation from a JSON string
active_courier_location_instance = ActiveCourierLocation.from_json(json)
# print the JSON string representation of the object
print(ActiveCourierLocation.to_json())

# convert the object into a dict
active_courier_location_dict = active_courier_location_instance.to_dict()
# create an instance of ActiveCourierLocation from a dict
active_courier_location_from_dict = ActiveCourierLocation.from_dict(active_courier_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


