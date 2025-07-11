# NetCustomerCreateOrUpdateCustomerResponse

Create or update customer response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer id. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_create_or_update_customer_response import NetCustomerCreateOrUpdateCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerCreateOrUpdateCustomerResponse from a JSON string
net_customer_create_or_update_customer_response_instance = NetCustomerCreateOrUpdateCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(NetCustomerCreateOrUpdateCustomerResponse.to_json())

# convert the object into a dict
net_customer_create_or_update_customer_response_dict = net_customer_create_or_update_customer_response_instance.to_dict()
# create an instance of NetCustomerCreateOrUpdateCustomerResponse from a dict
net_customer_create_or_update_customer_response_from_dict = NetCustomerCreateOrUpdateCustomerResponse.from_dict(net_customer_create_or_update_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


