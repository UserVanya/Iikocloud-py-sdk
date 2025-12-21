# CustomerRestoreCustomersResponse

Restore customers response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of unique customer IDs. | [optional] 
**restored** | **int** | Number of restored customers. | [optional] 
**not_found** | **int** | Number of unfound customers. | [optional] 

## Example

```python
from iikocloud_client.models.customer_restore_customers_response import CustomerRestoreCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerRestoreCustomersResponse from a JSON string
customer_restore_customers_response_instance = CustomerRestoreCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerRestoreCustomersResponse.to_json())

# convert the object into a dict
customer_restore_customers_response_dict = customer_restore_customers_response_instance.to_dict()
# create an instance of CustomerRestoreCustomersResponse from a dict
customer_restore_customers_response_from_dict = CustomerRestoreCustomersResponse.from_dict(customer_restore_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


