# NetCustomerDeleteCustomersRequest

Delete customers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[str]** | Customer IDs for logical deletion. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_customer_delete_customers_request import NetCustomerDeleteCustomersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerDeleteCustomersRequest from a JSON string
net_customer_delete_customers_request_instance = NetCustomerDeleteCustomersRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerDeleteCustomersRequest.to_json())

# convert the object into a dict
net_customer_delete_customers_request_dict = net_customer_delete_customers_request_instance.to_dict()
# create an instance of NetCustomerDeleteCustomersRequest from a dict
net_customer_delete_customers_request_from_dict = NetCustomerDeleteCustomersRequest.from_dict(net_customer_delete_customers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


