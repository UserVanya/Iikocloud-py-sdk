# CardTipsPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No. | [optional] 

## Example

```python
from iikocloud_client.models.card_tips_payment import CardTipsPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CardTipsPayment from a JSON string
card_tips_payment_instance = CardTipsPayment.from_json(json)
# print the JSON string representation of the object
print(CardTipsPayment.to_json())

# convert the object into a dict
card_tips_payment_dict = card_tips_payment_instance.to_dict()
# create an instance of CardTipsPayment from a dict
card_tips_payment_from_dict = CardTipsPayment.from_dict(card_tips_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


