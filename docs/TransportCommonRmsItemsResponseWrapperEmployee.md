# TransportCommonRmsItemsResponseWrapperEmployee

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportEmployeesEmployee]**](TransportEmployeesEmployee.md) | Items for organization. | 

## Example

```python
from iiko_cloud_client.models.transport_common_rms_items_response_wrapper_employee import TransportCommonRmsItemsResponseWrapperEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonRmsItemsResponseWrapperEmployee from a JSON string
transport_common_rms_items_response_wrapper_employee_instance = TransportCommonRmsItemsResponseWrapperEmployee.from_json(json)
# print the JSON string representation of the object
print(TransportCommonRmsItemsResponseWrapperEmployee.to_json())

# convert the object into a dict
transport_common_rms_items_response_wrapper_employee_dict = transport_common_rms_items_response_wrapper_employee_instance.to_dict()
# create an instance of TransportCommonRmsItemsResponseWrapperEmployee from a dict
transport_common_rms_items_response_wrapper_employee_from_dict = TransportCommonRmsItemsResponseWrapperEmployee.from_dict(transport_common_rms_items_response_wrapper_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


