# NetCustomerGetCustomerInfoByPhoneRequest

Request to get customer by phone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Customer phone number. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_get_customer_info_by_phone_request import NetCustomerGetCustomerInfoByPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCustomerInfoByPhoneRequest from a JSON string
net_customer_get_customer_info_by_phone_request_instance = NetCustomerGetCustomerInfoByPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCustomerInfoByPhoneRequest.to_json())

# convert the object into a dict
net_customer_get_customer_info_by_phone_request_dict = net_customer_get_customer_info_by_phone_request_instance.to_dict()
# create an instance of NetCustomerGetCustomerInfoByPhoneRequest from a dict
net_customer_get_customer_info_by_phone_request_from_dict = NetCustomerGetCustomerInfoByPhoneRequest.from_dict(net_customer_get_customer_info_by_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


