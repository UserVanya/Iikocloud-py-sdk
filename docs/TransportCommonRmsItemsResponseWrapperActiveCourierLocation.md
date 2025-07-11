# TransportCommonRmsItemsResponseWrapperActiveCourierLocation

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportEmployeesActiveCourierLocation]**](TransportEmployeesActiveCourierLocation.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.transport_common_rms_items_response_wrapper_active_courier_location import TransportCommonRmsItemsResponseWrapperActiveCourierLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonRmsItemsResponseWrapperActiveCourierLocation from a JSON string
transport_common_rms_items_response_wrapper_active_courier_location_instance = TransportCommonRmsItemsResponseWrapperActiveCourierLocation.from_json(json)
# print the JSON string representation of the object
print(TransportCommonRmsItemsResponseWrapperActiveCourierLocation.to_json())

# convert the object into a dict
transport_common_rms_items_response_wrapper_active_courier_location_dict = transport_common_rms_items_response_wrapper_active_courier_location_instance.to_dict()
# create an instance of TransportCommonRmsItemsResponseWrapperActiveCourierLocation from a dict
transport_common_rms_items_response_wrapper_active_courier_location_from_dict = TransportCommonRmsItemsResponseWrapperActiveCourierLocation.from_dict(transport_common_rms_items_response_wrapper_active_courier_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


