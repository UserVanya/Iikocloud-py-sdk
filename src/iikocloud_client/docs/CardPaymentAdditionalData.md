# CardPaymentAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | Card type (VISA, MasterCard, etc...).   &gt; Allowed from version &#x60;9.3.6&#x60;. | [optional] 
**custom_data** | **str** | Custom data.   &gt; Allowed from version &#x60;8.8.6&#x60;. | [optional] 
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No.  If this property is set, the above &#x60;number&#x60; property is ignored. | [optional] 

## Example

```python
from iikocloud_client.models.card_payment_additional_data import CardPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of CardPaymentAdditionalData from a JSON string
card_payment_additional_data_instance = CardPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(CardPaymentAdditionalData.to_json())

# convert the object into a dict
card_payment_additional_data_dict = card_payment_additional_data_instance.to_dict()
# create an instance of CardPaymentAdditionalData from a dict
card_payment_additional_data_from_dict = CardPaymentAdditionalData.from_dict(card_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


