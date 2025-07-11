# TransportDeliveriesRequestCreateOrderCardPayment

Bank card payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_card_payment import TransportDeliveriesRequestCreateOrderCardPayment

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderCardPayment from a JSON string
transport_deliveries_request_create_order_card_payment_instance = TransportDeliveriesRequestCreateOrderCardPayment.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderCardPayment.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_card_payment_dict = transport_deliveries_request_create_order_card_payment_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderCardPayment from a dict
transport_deliveries_request_create_order_card_payment_from_dict = TransportDeliveriesRequestCreateOrderCardPayment.from_dict(transport_deliveries_request_create_order_card_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


