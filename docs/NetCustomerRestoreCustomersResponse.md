# NetCustomerRestoreCustomersResponse

Restore customers response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of unique customer IDs. | [optional] 
**restored** | **int** | Number of restored customers. | [optional] 
**not_found** | **int** | Number of unfound customers. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_restore_customers_response import NetCustomerRestoreCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerRestoreCustomersResponse from a JSON string
net_customer_restore_customers_response_instance = NetCustomerRestoreCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(NetCustomerRestoreCustomersResponse.to_json())

# convert the object into a dict
net_customer_restore_customers_response_dict = net_customer_restore_customers_response_instance.to_dict()
# create an instance of NetCustomerRestoreCustomersResponse from a dict
net_customer_restore_customers_response_from_dict = NetCustomerRestoreCustomersResponse.from_dict(net_customer_restore_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


