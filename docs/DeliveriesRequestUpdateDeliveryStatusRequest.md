# DeliveriesRequestUpdateDeliveryStatusRequest

Request for delivery status update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**delivery_status** | [**DeliveriesCommonDeliveryStatusForUpdate**](DeliveriesCommonDeliveryStatusForUpdate.md) | Delivery status. Can be only switched between these three statuses. | 
**delivery_date** | **str** | The date and time when the order was received by the guest (Local for delivery terminal). | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_update_delivery_status_request import DeliveriesRequestUpdateDeliveryStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateDeliveryStatusRequest from a JSON string
deliveries_request_update_delivery_status_request_instance = DeliveriesRequestUpdateDeliveryStatusRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateDeliveryStatusRequest.to_json())

# convert the object into a dict
deliveries_request_update_delivery_status_request_dict = deliveries_request_update_delivery_status_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateDeliveryStatusRequest from a dict
deliveries_request_update_delivery_status_request_from_dict = DeliveriesRequestUpdateDeliveryStatusRequest.from_dict(deliveries_request_update_delivery_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


