# TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest

Request for confirm delivery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_order_confirm_delivery_request import TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest from a JSON string
transport_deliveries_request_update_order_confirm_delivery_request_instance = TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_confirm_delivery_request_dict = transport_deliveries_request_update_order_confirm_delivery_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest from a dict
transport_deliveries_request_update_order_confirm_delivery_request_from_dict = TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest.from_dict(transport_deliveries_request_update_order_confirm_delivery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


