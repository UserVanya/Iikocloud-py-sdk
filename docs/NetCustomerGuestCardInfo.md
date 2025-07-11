# NetCustomerGuestCardInfo

Guest card info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Card id. | [optional] 
**track** | **str** | Card track. | [optional] 
**number** | **str** | Card number. | [optional] 
**valid_to_date** | **str** | Card valid to date. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_guest_card_info import NetCustomerGuestCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGuestCardInfo from a JSON string
net_customer_guest_card_info_instance = NetCustomerGuestCardInfo.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGuestCardInfo.to_json())

# convert the object into a dict
net_customer_guest_card_info_dict = net_customer_guest_card_info_instance.to_dict()
# create an instance of NetCustomerGuestCardInfo from a dict
net_customer_guest_card_info_from_dict = NetCustomerGuestCardInfo.from_dict(net_customer_guest_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


