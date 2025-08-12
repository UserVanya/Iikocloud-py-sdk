# TransportDeliveriesRequestUpdateOrderChangePaymentsRequest

Change order's payments request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**payments** | [**List[TransportDeliveriesRequestCreateOrderPayment]**](TransportDeliveriesRequestCreateOrderPayment.md) | Order payments. | 
**tips** | [**List[TransportDeliveriesRequestCreateOrderTipsPayment]**](TransportDeliveriesRequestCreateOrderTipsPayment.md) | Order tips. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_order_change_payments_request import TransportDeliveriesRequestUpdateOrderChangePaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangePaymentsRequest from a JSON string
transport_deliveries_request_update_order_change_payments_request_instance = TransportDeliveriesRequestUpdateOrderChangePaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangePaymentsRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_payments_request_dict = transport_deliveries_request_update_order_change_payments_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangePaymentsRequest from a dict
transport_deliveries_request_update_order_change_payments_request_from_dict = TransportDeliveriesRequestUpdateOrderChangePaymentsRequest.from_dict(transport_deliveries_request_update_order_change_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


