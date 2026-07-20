# DeleteCustomersResponse

Delete customers response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **int** | Number of deleted customers. | [optional] 
**not_found** | **int** | Number of not found customers. | [optional] 
**total** | **int** | Number of unique customer IDs. | [optional] 

## Example

```python
from iikocloud_client.models.delete_customers_response import DeleteCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustomersResponse from a JSON string
delete_customers_response_instance = DeleteCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteCustomersResponse.to_json())

# convert the object into a dict
delete_customers_response_dict = delete_customers_response_instance.to_dict()
# create an instance of DeleteCustomersResponse from a dict
delete_customers_response_from_dict = DeleteCustomersResponse.from_dict(delete_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


