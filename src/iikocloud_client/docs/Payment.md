# Payment

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

## Example

```python
from iikocloud_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


