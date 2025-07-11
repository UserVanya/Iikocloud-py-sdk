# TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportEmployeesEmployeeWithCheckedRole]**](TransportEmployeesEmployeeWithCheckedRole.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.transport_common_rms_items_response_wrapper_employee_with_checked_role import TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole from a JSON string
transport_common_rms_items_response_wrapper_employee_with_checked_role_instance = TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole.from_json(json)
# print the JSON string representation of the object
print(TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole.to_json())

# convert the object into a dict
transport_common_rms_items_response_wrapper_employee_with_checked_role_dict = transport_common_rms_items_response_wrapper_employee_with_checked_role_instance.to_dict()
# create an instance of TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole from a dict
transport_common_rms_items_response_wrapper_employee_with_checked_role_from_dict = TransportCommonRmsItemsResponseWrapperEmployeeWithCheckedRole.from_dict(transport_common_rms_items_response_wrapper_employee_with_checked_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


