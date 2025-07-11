# NetCustomerGetCustomerInfoByCardNumberRequest

Request to get customer by card number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Customer card number. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_get_customer_info_by_card_number_request import NetCustomerGetCustomerInfoByCardNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCustomerInfoByCardNumberRequest from a JSON string
net_customer_get_customer_info_by_card_number_request_instance = NetCustomerGetCustomerInfoByCardNumberRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCustomerInfoByCardNumberRequest.to_json())

# convert the object into a dict
net_customer_get_customer_info_by_card_number_request_dict = net_customer_get_customer_info_by_card_number_request_instance.to_dict()
# create an instance of NetCustomerGetCustomerInfoByCardNumberRequest from a dict
net_customer_get_customer_info_by_card_number_request_from_dict = NetCustomerGetCustomerInfoByCardNumberRequest.from_dict(net_customer_get_customer_info_by_card_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


