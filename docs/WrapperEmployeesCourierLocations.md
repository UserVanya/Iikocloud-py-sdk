# WrapperEmployeesCourierLocations

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[EmployeesCourierLocations]**](EmployeesCourierLocations.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_employees_courier_locations import WrapperEmployeesCourierLocations

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperEmployeesCourierLocations from a JSON string
wrapper_employees_courier_locations_instance = WrapperEmployeesCourierLocations.from_json(json)
# print the JSON string representation of the object
print(WrapperEmployeesCourierLocations.to_json())

# convert the object into a dict
wrapper_employees_courier_locations_dict = wrapper_employees_courier_locations_instance.to_dict()
# create an instance of WrapperEmployeesCourierLocations from a dict
wrapper_employees_courier_locations_from_dict = WrapperEmployeesCourierLocations.from_dict(wrapper_employees_courier_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


