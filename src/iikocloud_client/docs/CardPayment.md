# CardPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No. | [optional] 

## Example

```python
from iikocloud_client.models.card_payment import CardPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CardPayment from a JSON string
card_payment_instance = CardPayment.from_json(json)
# print the JSON string representation of the object
print(CardPayment.to_json())

# convert the object into a dict
card_payment_dict = card_payment_instance.to_dict()
# create an instance of CardPayment from a dict
card_payment_from_dict = CardPayment.from_dict(card_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


