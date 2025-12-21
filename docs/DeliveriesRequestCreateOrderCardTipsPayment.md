# DeliveriesRequestCreateOrderCardTipsPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_card_tips_payment import DeliveriesRequestCreateOrderCardTipsPayment

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderCardTipsPayment from a JSON string
deliveries_request_create_order_card_tips_payment_instance = DeliveriesRequestCreateOrderCardTipsPayment.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderCardTipsPayment.to_json())

# convert the object into a dict
deliveries_request_create_order_card_tips_payment_dict = deliveries_request_create_order_card_tips_payment_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderCardTipsPayment from a dict
deliveries_request_create_order_card_tips_payment_from_dict = DeliveriesRequestCreateOrderCardTipsPayment.from_dict(deliveries_request_create_order_card_tips_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


