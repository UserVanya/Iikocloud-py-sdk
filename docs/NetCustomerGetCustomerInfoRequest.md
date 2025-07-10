# NetCustomerGetCustomerInfoRequest

Base class for customer info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**organization_id** | **str** | Organization id. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_customer_get_customer_info_request import NetCustomerGetCustomerInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCustomerInfoRequest from a JSON string
net_customer_get_customer_info_request_instance = NetCustomerGetCustomerInfoRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCustomerInfoRequest.to_json())

# convert the object into a dict
net_customer_get_customer_info_request_dict = net_customer_get_customer_info_request_instance.to_dict()
# create an instance of NetCustomerGetCustomerInfoRequest from a dict
net_customer_get_customer_info_request_from_dict = NetCustomerGetCustomerInfoRequest.from_dict(net_customer_get_customer_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


