# AvailablePayment

Available payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Marketing campaign id. | [optional] 
**max_sum** | **float** | Max sum. | [optional] 
**order** | **int** | Payment order. In case of partial payment, payments with lesser order should be filled first. | [optional] 
**wallet_infos** | [**List[WalletInfo]**](WalletInfo.md) | Wallet infos. | [optional] 

## Example

```python
from iikocloud_client.models.available_payment import AvailablePayment

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePayment from a JSON string
available_payment_instance = AvailablePayment.from_json(json)
# print the JSON string representation of the object
print(AvailablePayment.to_json())

# convert the object into a dict
available_payment_dict = available_payment_instance.to_dict()
# create an instance of AvailablePayment from a dict
available_payment_from_dict = AvailablePayment.from_dict(available_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


