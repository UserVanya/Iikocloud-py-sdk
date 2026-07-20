# TipsPaymentItem

Delivery order tips payment component.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_external** | **bool** | Payment item is external (created via biz.API). | 
**is_fiscalized_externally** | **bool** | Whether the payment item is externally fiscalized.   &gt; Allowed from version &#x60;7.6.3&#x60;. | [optional] 
**is_preliminary** | **bool** | Whether payment item is preliminary. | 
**is_prepay** | **bool** | Whether the payment item is prepay.   &gt; Allowed from version &#x60;7.7.6&#x60;. | 
**is_processed_externally** | **bool** | Payment item is processed by external payment system. | 
**payment_type** | [**DeliveryOrderResponsePaymentType**](DeliveryOrderResponsePaymentType.md) | Payment type.                 Can be obtained by &#x60;/api/1/payment_types&#x60; operation. | 
**sum** | **float** | Amount due. | 
**tips_type** | [**DeliveryOrderResponseTipsType**](DeliveryOrderResponseTipsType.md) | Tips type. | [optional] 

## Example

```python
from iikocloud_client.models.tips_payment_item import TipsPaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of TipsPaymentItem from a JSON string
tips_payment_item_instance = TipsPaymentItem.from_json(json)
# print the JSON string representation of the object
print(TipsPaymentItem.to_json())

# convert the object into a dict
tips_payment_item_dict = tips_payment_item_instance.to_dict()
# create an instance of TipsPaymentItem from a dict
tips_payment_item_from_dict = TipsPaymentItem.from_dict(tips_payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


