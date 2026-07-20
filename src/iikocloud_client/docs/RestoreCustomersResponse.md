# RestoreCustomersResponse

Restore customers response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_found** | **int** | Number of not found customers. | [optional] 
**restored** | **int** | Number of restored customers. | [optional] 
**total** | **int** | Number of unique customer IDs. | [optional] 

## Example

```python
from iikocloud_client.models.restore_customers_response import RestoreCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreCustomersResponse from a JSON string
restore_customers_response_instance = RestoreCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(RestoreCustomersResponse.to_json())

# convert the object into a dict
restore_customers_response_dict = restore_customers_response_instance.to_dict()
# create an instance of RestoreCustomersResponse from a dict
restore_customers_response_from_dict = RestoreCustomersResponse.from_dict(restore_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


