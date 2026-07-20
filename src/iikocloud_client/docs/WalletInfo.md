# WalletInfo

Wallet info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_hold_money** | **bool** | Can hold money. | [optional] 
**id** | **UUID** | Wallet id. | [optional] 
**max_sum** | **float** | Max sum for payment from the wallet. | [optional] 

## Example

```python
from iikocloud_client.models.wallet_info import WalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WalletInfo from a JSON string
wallet_info_instance = WalletInfo.from_json(json)
# print the JSON string representation of the object
print(WalletInfo.to_json())

# convert the object into a dict
wallet_info_dict = wallet_info_instance.to_dict()
# create an instance of WalletInfo from a dict
wallet_info_from_dict = WalletInfo.from_dict(wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


