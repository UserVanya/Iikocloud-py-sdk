# RmsCourierLocationsItemsResponse

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CourierLocations]**](CourierLocations.md) | Items for organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.rms_courier_locations_items_response import RmsCourierLocationsItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RmsCourierLocationsItemsResponse from a JSON string
rms_courier_locations_items_response_instance = RmsCourierLocationsItemsResponse.from_json(json)
# print the JSON string representation of the object
print(RmsCourierLocationsItemsResponse.to_json())

# convert the object into a dict
rms_courier_locations_items_response_dict = rms_courier_locations_items_response_instance.to_dict()
# create an instance of RmsCourierLocationsItemsResponse from a dict
rms_courier_locations_items_response_from_dict = RmsCourierLocationsItemsResponse.from_dict(rms_courier_locations_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


