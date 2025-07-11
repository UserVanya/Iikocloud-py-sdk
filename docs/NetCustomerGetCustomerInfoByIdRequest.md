# NetCustomerGetCustomerInfoByIdRequest

Request to get customer by Id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer id. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_get_customer_info_by_id_request import NetCustomerGetCustomerInfoByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCustomerInfoByIdRequest from a JSON string
net_customer_get_customer_info_by_id_request_instance = NetCustomerGetCustomerInfoByIdRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCustomerInfoByIdRequest.to_json())

# convert the object into a dict
net_customer_get_customer_info_by_id_request_dict = net_customer_get_customer_info_by_id_request_instance.to_dict()
# create an instance of NetCustomerGetCustomerInfoByIdRequest from a dict
net_customer_get_customer_info_by_id_request_from_dict = NetCustomerGetCustomerInfoByIdRequest.from_dict(net_customer_get_customer_info_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


