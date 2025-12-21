# RmsItemsResponseWrapperEmployeesCourierLocations

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsEmployeesCourierLocations]**](IikoTransportPublicApiContractsEmployeesCourierLocations.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.rms_items_response_wrapper_employees_courier_locations import RmsItemsResponseWrapperEmployeesCourierLocations

# TODO update the JSON string below
json = "{}"
# create an instance of RmsItemsResponseWrapperEmployeesCourierLocations from a JSON string
rms_items_response_wrapper_employees_courier_locations_instance = RmsItemsResponseWrapperEmployeesCourierLocations.from_json(json)
# print the JSON string representation of the object
print(RmsItemsResponseWrapperEmployeesCourierLocations.to_json())

# convert the object into a dict
rms_items_response_wrapper_employees_courier_locations_dict = rms_items_response_wrapper_employees_courier_locations_instance.to_dict()
# create an instance of RmsItemsResponseWrapperEmployeesCourierLocations from a dict
rms_items_response_wrapper_employees_courier_locations_from_dict = RmsItemsResponseWrapperEmployeesCourierLocations.from_dict(rms_items_response_wrapper_employees_courier_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


