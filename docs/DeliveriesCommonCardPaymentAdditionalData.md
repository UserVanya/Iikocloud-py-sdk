# DeliveriesCommonCardPaymentAdditionalData

Additional data for Card payment item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No.  If this property is set, the above &#x60;number&#x60; property is ignored. | [optional] 
**custom_data** | **str** | Custom data.   &gt; Allowed from version &#x60;8.8.6&#x60;. | [optional] 
**card_type** | **str** | Card type (VISA, MasterCard, etc...).   &gt; Allowed from version &#x60;9.3.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_common_card_payment_additional_data import DeliveriesCommonCardPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesCommonCardPaymentAdditionalData from a JSON string
deliveries_common_card_payment_additional_data_instance = DeliveriesCommonCardPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(DeliveriesCommonCardPaymentAdditionalData.to_json())

# convert the object into a dict
deliveries_common_card_payment_additional_data_dict = deliveries_common_card_payment_additional_data_instance.to_dict()
# create an instance of DeliveriesCommonCardPaymentAdditionalData from a dict
deliveries_common_card_payment_additional_data_from_dict = DeliveriesCommonCardPaymentAdditionalData.from_dict(deliveries_common_card_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


