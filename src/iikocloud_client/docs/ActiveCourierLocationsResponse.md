# ActiveCourierLocationsResponse

Wrapping object to retrieve list of active courier locations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_courier_locations** | [**List[RmsActiveCourierLocationItemsResponse]**](RmsActiveCourierLocationItemsResponse.md) | List of courier&#39;s locations. | 
**correlation_id** | **UUID** | Operation ID. | 

## Example

```python
from iikocloud_client.models.active_courier_locations_response import ActiveCourierLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveCourierLocationsResponse from a JSON string
active_courier_locations_response_instance = ActiveCourierLocationsResponse.from_json(json)
# print the JSON string representation of the object
print(ActiveCourierLocationsResponse.to_json())

# convert the object into a dict
active_courier_locations_response_dict = active_courier_locations_response_instance.to_dict()
# create an instance of ActiveCourierLocationsResponse from a dict
active_courier_locations_response_from_dict = ActiveCourierLocationsResponse.from_dict(active_courier_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


