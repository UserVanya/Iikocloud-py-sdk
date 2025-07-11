# NetLoyaltyResultAvailablePayment

Available payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Marketing campaign id. | [optional] 
**max_sum** | **float** | Max sum. | [optional] 
**order** | **int** | Payment order. In case of partial payment, payments with lesser order should be filled first. | [optional] 
**wallet_infos** | [**List[NetLoyaltyResultWalletInfo]**](NetLoyaltyResultWalletInfo.md) | Wallet infos. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_available_payment import NetLoyaltyResultAvailablePayment

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultAvailablePayment from a JSON string
net_loyalty_result_available_payment_instance = NetLoyaltyResultAvailablePayment.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultAvailablePayment.to_json())

# convert the object into a dict
net_loyalty_result_available_payment_dict = net_loyalty_result_available_payment_instance.to_dict()
# create an instance of NetLoyaltyResultAvailablePayment from a dict
net_loyalty_result_available_payment_from_dict = NetLoyaltyResultAvailablePayment.from_dict(net_loyalty_result_available_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


