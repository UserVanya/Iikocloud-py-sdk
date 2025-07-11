# NetCustomerDeleteCustomersResponse

Delete customers response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of unique customer IDs. | [optional] 
**deleted** | **int** | Number of deleted customers. | [optional] 
**not_found** | **int** | Number of unfound customers. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_delete_customers_response import NetCustomerDeleteCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerDeleteCustomersResponse from a JSON string
net_customer_delete_customers_response_instance = NetCustomerDeleteCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(NetCustomerDeleteCustomersResponse.to_json())

# convert the object into a dict
net_customer_delete_customers_response_dict = net_customer_delete_customers_response_instance.to_dict()
# create an instance of NetCustomerDeleteCustomersResponse from a dict
net_customer_delete_customers_response_from_dict = NetCustomerDeleteCustomersResponse.from_dict(net_customer_delete_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


