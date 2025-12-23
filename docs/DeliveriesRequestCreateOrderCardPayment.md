# DeliveriesRequestCreateOrderCardPayment

Bank card payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Card No.  &gt; In iikoFront, it is possible to make card payment without card No. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_card_payment import DeliveriesRequestCreateOrderCardPayment

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderCardPayment from a JSON string
deliveries_request_create_order_card_payment_instance = DeliveriesRequestCreateOrderCardPayment.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderCardPayment.to_json())

# convert the object into a dict
deliveries_request_create_order_card_payment_dict = deliveries_request_create_order_card_payment_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderCardPayment from a dict
deliveries_request_create_order_card_payment_from_dict = DeliveriesRequestCreateOrderCardPayment.from_dict(deliveries_request_create_order_card_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


