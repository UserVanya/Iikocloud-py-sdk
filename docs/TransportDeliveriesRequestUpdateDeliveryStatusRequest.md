# TransportDeliveriesRequestUpdateDeliveryStatusRequest

Request for delivery status update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**delivery_status** | [**TransportDeliveriesCommonDeliveryStatusForUpdate**](TransportDeliveriesCommonDeliveryStatusForUpdate.md) | Delivery status. Can be only switched between these three statuses. | 
**delivery_date** | **str** | The date and time when the order was received by the guest (Local for delivery terminal). | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_delivery_status_request import TransportDeliveriesRequestUpdateDeliveryStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateDeliveryStatusRequest from a JSON string
transport_deliveries_request_update_delivery_status_request_instance = TransportDeliveriesRequestUpdateDeliveryStatusRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateDeliveryStatusRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_delivery_status_request_dict = transport_deliveries_request_update_delivery_status_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateDeliveryStatusRequest from a dict
transport_deliveries_request_update_delivery_status_request_from_dict = TransportDeliveriesRequestUpdateDeliveryStatusRequest.from_dict(transport_deliveries_request_update_delivery_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


