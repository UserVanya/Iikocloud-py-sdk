# TipsPayment

Base class of delivery order payment item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_fiscalized_externally** | **bool** | Whether the payment item is externally fiscalized.   &gt; Allowed from version &#x60;7.6.3&#x60;. | [optional] 
**is_prepay** | **bool** | Whether the payment item is prepay. Unavailable for &#x60;paymentKindType.LoyaltyCard&#x60;.   &gt; Allowed from version &#x60;8.2.6&#x60;. | [optional] 
**is_processed_externally** | **bool** | Whether payment item is processed by external payment system (made from outside). | [optional] 
**payment_additional_data** | [**PaymentAdditionalData**](PaymentAdditionalData.md) | Additional payment parameters. | [optional] 
**payment_type_id** | **UUID** | Payment type.                 Can be obtained by &#x60;/api/1/payment_types&#x60; operation. | 
**payment_type_kind** | **str** |  | 
**sum** | **float** | Amount due. | 
**tips_type_id** | **UUID** | Tips type ID.                Can be obtained by &#x60;/api/1/tips_types&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.tips_payment import TipsPayment

# TODO update the JSON string below
json = "{}"
# create an instance of TipsPayment from a JSON string
tips_payment_instance = TipsPayment.from_json(json)
# print the JSON string representation of the object
print(TipsPayment.to_json())

# convert the object into a dict
tips_payment_dict = tips_payment_instance.to_dict()
# create an instance of TipsPayment from a dict
tips_payment_from_dict = TipsPayment.from_dict(tips_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


