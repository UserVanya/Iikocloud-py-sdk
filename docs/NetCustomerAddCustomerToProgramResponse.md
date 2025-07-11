# NetCustomerAddCustomerToProgramResponse

Add customer to program response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_wallet_id** | **str** | User wallet id. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_add_customer_to_program_response import NetCustomerAddCustomerToProgramResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerAddCustomerToProgramResponse from a JSON string
net_customer_add_customer_to_program_response_instance = NetCustomerAddCustomerToProgramResponse.from_json(json)
# print the JSON string representation of the object
print(NetCustomerAddCustomerToProgramResponse.to_json())

# convert the object into a dict
net_customer_add_customer_to_program_response_dict = net_customer_add_customer_to_program_response_instance.to_dict()
# create an instance of NetCustomerAddCustomerToProgramResponse from a dict
net_customer_add_customer_to_program_response_from_dict = NetCustomerAddCustomerToProgramResponse.from_dict(net_customer_add_customer_to_program_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


