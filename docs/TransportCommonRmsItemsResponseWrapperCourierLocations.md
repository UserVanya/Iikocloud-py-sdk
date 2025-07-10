# TransportCommonRmsItemsResponseWrapperCourierLocations

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportEmployeesCourierLocations]**](TransportEmployeesCourierLocations.md) | Items for organization. | 

## Example

```python
from iiko_cloud_client.models.transport_common_rms_items_response_wrapper_courier_locations import TransportCommonRmsItemsResponseWrapperCourierLocations

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonRmsItemsResponseWrapperCourierLocations from a JSON string
transport_common_rms_items_response_wrapper_courier_locations_instance = TransportCommonRmsItemsResponseWrapperCourierLocations.from_json(json)
# print the JSON string representation of the object
print(TransportCommonRmsItemsResponseWrapperCourierLocations.to_json())

# convert the object into a dict
transport_common_rms_items_response_wrapper_courier_locations_dict = transport_common_rms_items_response_wrapper_courier_locations_instance.to_dict()
# create an instance of TransportCommonRmsItemsResponseWrapperCourierLocations from a dict
transport_common_rms_items_response_wrapper_courier_locations_from_dict = TransportCommonRmsItemsResponseWrapperCourierLocations.from_dict(transport_common_rms_items_response_wrapper_courier_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


