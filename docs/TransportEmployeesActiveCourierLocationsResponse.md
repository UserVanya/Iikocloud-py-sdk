# TransportEmployeesActiveCourierLocationsResponse

Wrapping object to retrieve list of active courier locations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**active_courier_locations** | [**List[TransportCommonRmsItemsResponseWrapperActiveCourierLocation]**](TransportCommonRmsItemsResponseWrapperActiveCourierLocation.md) | List of courier&#39;s locations. | 

## Example

```python
from iikocloud_client.models.transport_employees_active_courier_locations_response import TransportEmployeesActiveCourierLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesActiveCourierLocationsResponse from a JSON string
transport_employees_active_courier_locations_response_instance = TransportEmployeesActiveCourierLocationsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesActiveCourierLocationsResponse.to_json())

# convert the object into a dict
transport_employees_active_courier_locations_response_dict = transport_employees_active_courier_locations_response_instance.to_dict()
# create an instance of TransportEmployeesActiveCourierLocationsResponse from a dict
transport_employees_active_courier_locations_response_from_dict = TransportEmployeesActiveCourierLocationsResponse.from_dict(transport_employees_active_courier_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


