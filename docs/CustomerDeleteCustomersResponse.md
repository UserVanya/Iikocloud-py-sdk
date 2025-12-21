# CustomerDeleteCustomersResponse

Delete customers response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of unique customer IDs. | [optional] 
**deleted** | **int** | Number of deleted customers. | [optional] 
**not_found** | **int** | Number of unfound customers. | [optional] 

## Example

```python
from iikocloud_client.models.customer_delete_customers_response import CustomerDeleteCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerDeleteCustomersResponse from a JSON string
customer_delete_customers_response_instance = CustomerDeleteCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerDeleteCustomersResponse.to_json())

# convert the object into a dict
customer_delete_customers_response_dict = customer_delete_customers_response_instance.to_dict()
# create an instance of CustomerDeleteCustomersResponse from a dict
customer_delete_customers_response_from_dict = CustomerDeleteCustomersResponse.from_dict(customer_delete_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


