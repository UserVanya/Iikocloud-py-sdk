# TransportDeliveriesRequestUpdateOrderPaymentsRequest

Request for order payment update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**payment_items** | [**List[TransportDeliveriesRequestUpdateOrderOrderPaymentItem]**](TransportDeliveriesRequestUpdateOrderOrderPaymentItem.md) | Payment details. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_order_payments_request import TransportDeliveriesRequestUpdateOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderPaymentsRequest from a JSON string
transport_deliveries_request_update_order_payments_request_instance = TransportDeliveriesRequestUpdateOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderPaymentsRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_payments_request_dict = transport_deliveries_request_update_order_payments_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderPaymentsRequest from a dict
transport_deliveries_request_update_order_payments_request_from_dict = TransportDeliveriesRequestUpdateOrderPaymentsRequest.from_dict(transport_deliveries_request_update_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


