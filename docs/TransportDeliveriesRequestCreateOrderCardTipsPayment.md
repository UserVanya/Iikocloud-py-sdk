# TransportDeliveriesRequestCreateOrderCardTipsPayment

Bank card tips payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_card_tips_payment import TransportDeliveriesRequestCreateOrderCardTipsPayment

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderCardTipsPayment from a JSON string
transport_deliveries_request_create_order_card_tips_payment_instance = TransportDeliveriesRequestCreateOrderCardTipsPayment.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderCardTipsPayment.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_card_tips_payment_dict = transport_deliveries_request_create_order_card_tips_payment_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderCardTipsPayment from a dict
transport_deliveries_request_create_order_card_tips_payment_from_dict = TransportDeliveriesRequestCreateOrderCardTipsPayment.from_dict(transport_deliveries_request_create_order_card_tips_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


