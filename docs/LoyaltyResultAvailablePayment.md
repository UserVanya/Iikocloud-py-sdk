# LoyaltyResultAvailablePayment

Available payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Marketing campaign id. | [optional] 
**max_sum** | **float** | Max sum. | [optional] 
**order** | **int** | Payment order. In case of partial payment, payments with lesser order should be filled first. | [optional] 
**wallet_infos** | [**List[LoyaltyResultWalletInfo]**](LoyaltyResultWalletInfo.md) | Wallet infos. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_available_payment import LoyaltyResultAvailablePayment

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultAvailablePayment from a JSON string
loyalty_result_available_payment_instance = LoyaltyResultAvailablePayment.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultAvailablePayment.to_json())

# convert the object into a dict
loyalty_result_available_payment_dict = loyalty_result_available_payment_instance.to_dict()
# create an instance of LoyaltyResultAvailablePayment from a dict
loyalty_result_available_payment_from_dict = LoyaltyResultAvailablePayment.from_dict(loyalty_result_available_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


