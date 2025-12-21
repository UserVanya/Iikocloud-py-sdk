# DeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest

Request for cancel delivery confirmation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_cancel_delivery_confirmation_request import DeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest from a JSON string
deliveries_request_update_order_cancel_delivery_confirmation_request_instance = DeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_cancel_delivery_confirmation_request_dict = deliveries_request_update_order_cancel_delivery_confirmation_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest from a dict
deliveries_request_update_order_cancel_delivery_confirmation_request_from_dict = DeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.from_dict(deliveries_request_update_order_cancel_delivery_confirmation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


