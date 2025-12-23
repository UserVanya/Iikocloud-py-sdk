# LoyaltyResultWalletInfo

Wallet info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Wallet id. | [optional] 
**max_sum** | **float** | Max sum for payment from the wallet. | [optional] 
**can_hold_money** | **bool** | Can hold money. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_wallet_info import LoyaltyResultWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultWalletInfo from a JSON string
loyalty_result_wallet_info_instance = LoyaltyResultWalletInfo.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultWalletInfo.to_json())

# convert the object into a dict
loyalty_result_wallet_info_dict = loyalty_result_wallet_info_instance.to_dict()
# create an instance of LoyaltyResultWalletInfo from a dict
loyalty_result_wallet_info_from_dict = LoyaltyResultWalletInfo.from_dict(loyalty_result_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


