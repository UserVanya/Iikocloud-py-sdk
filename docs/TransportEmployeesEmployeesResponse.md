# TransportEmployeesEmployeesResponse

Wrapping object to retrieve list of drivers from iikoRMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**employees** | [**List[TransportCommonRmsItemsResponseWrapperEmployee]**](TransportCommonRmsItemsResponseWrapperEmployee.md) | List of drivers. | 

## Example

```python
from iiko_cloud_client.models.transport_employees_employees_response import TransportEmployeesEmployeesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesEmployeesResponse from a JSON string
transport_employees_employees_response_instance = TransportEmployeesEmployeesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesEmployeesResponse.to_json())

# convert the object into a dict
transport_employees_employees_response_dict = transport_employees_employees_response_instance.to_dict()
# create an instance of TransportEmployeesEmployeesResponse from a dict
transport_employees_employees_response_from_dict = TransportEmployeesEmployeesResponse.from_dict(transport_employees_employees_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


