# NetLoyaltyResultWalletInfo

Wallet info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Wallet id. | [optional] 
**max_sum** | **float** | Max sum for payment from the wallet. | [optional] 
**can_hold_money** | **bool** | Can hold money. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_wallet_info import NetLoyaltyResultWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultWalletInfo from a JSON string
net_loyalty_result_wallet_info_instance = NetLoyaltyResultWalletInfo.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultWalletInfo.to_json())

# convert the object into a dict
net_loyalty_result_wallet_info_dict = net_loyalty_result_wallet_info_instance.to_dict()
# create an instance of NetLoyaltyResultWalletInfo from a dict
net_loyalty_result_wallet_info_from_dict = NetLoyaltyResultWalletInfo.from_dict(net_loyalty_result_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


