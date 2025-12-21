# RmsItemsResponseWrapperEmployeesEmployee

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsEmployeesEmployee]**](IikoTransportPublicApiContractsEmployeesEmployee.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.rms_items_response_wrapper_employees_employee import RmsItemsResponseWrapperEmployeesEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of RmsItemsResponseWrapperEmployeesEmployee from a JSON string
rms_items_response_wrapper_employees_employee_instance = RmsItemsResponseWrapperEmployeesEmployee.from_json(json)
# print the JSON string representation of the object
print(RmsItemsResponseWrapperEmployeesEmployee.to_json())

# convert the object into a dict
rms_items_response_wrapper_employees_employee_dict = rms_items_response_wrapper_employees_employee_instance.to_dict()
# create an instance of RmsItemsResponseWrapperEmployeesEmployee from a dict
rms_items_response_wrapper_employees_employee_from_dict = RmsItemsResponseWrapperEmployeesEmployee.from_dict(rms_items_response_wrapper_employees_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


