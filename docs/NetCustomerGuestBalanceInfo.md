# NetCustomerGuestBalanceInfo

Information about guest balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Wallet id. | [optional] 
**name** | **str** | Wallet name. | [optional] 
**type** | [**NetProgramType**](NetProgramType.md) | Wallet type.  &lt;br&gt;0 - deposit or corporate nutrition,&lt;br /&gt;1 - bonus program,&lt;br /&gt;2 - products program,&lt;br /&gt;3 - discount program,&lt;br /&gt;4 - certificate program. | [optional] 
**balance** | **float** | Wallet balance. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_guest_balance_info import NetCustomerGuestBalanceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGuestBalanceInfo from a JSON string
net_customer_guest_balance_info_instance = NetCustomerGuestBalanceInfo.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGuestBalanceInfo.to_json())

# convert the object into a dict
net_customer_guest_balance_info_dict = net_customer_guest_balance_info_instance.to_dict()
# create an instance of NetCustomerGuestBalanceInfo from a dict
net_customer_guest_balance_info_from_dict = NetCustomerGuestBalanceInfo.from_dict(net_customer_guest_balance_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


