# NetCustomerAddCustomerToProgramRequest

Add customer to program request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id. | [optional] 
**program_id** | **str** | Program id. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_customer_add_customer_to_program_request import NetCustomerAddCustomerToProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerAddCustomerToProgramRequest from a JSON string
net_customer_add_customer_to_program_request_instance = NetCustomerAddCustomerToProgramRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerAddCustomerToProgramRequest.to_json())

# convert the object into a dict
net_customer_add_customer_to_program_request_dict = net_customer_add_customer_to_program_request_instance.to_dict()
# create an instance of NetCustomerAddCustomerToProgramRequest from a dict
net_customer_add_customer_to_program_request_from_dict = NetCustomerAddCustomerToProgramRequest.from_dict(net_customer_add_customer_to_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


