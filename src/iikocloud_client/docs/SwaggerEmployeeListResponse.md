# SwaggerEmployeeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmployeeResponse]**](EmployeeResponse.md) | Employees | [optional] 
**limit** | **int** | Maximum number of records in the response. | [optional] 
**offset** | **int** | Number of records to skip from the beginning. | [optional] 
**total_count** | **int** | Total number of employees | [optional] 

## Example

```python
from iikocloud_client.models.swagger_employee_list_response import SwaggerEmployeeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerEmployeeListResponse from a JSON string
swagger_employee_list_response_instance = SwaggerEmployeeListResponse.from_json(json)
# print the JSON string representation of the object
print(SwaggerEmployeeListResponse.to_json())

# convert the object into a dict
swagger_employee_list_response_dict = swagger_employee_list_response_instance.to_dict()
# create an instance of SwaggerEmployeeListResponse from a dict
swagger_employee_list_response_from_dict = SwaggerEmployeeListResponse.from_dict(swagger_employee_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


