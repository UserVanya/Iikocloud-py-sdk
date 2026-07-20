# UpdateDeliveryStatusRequest

Request for delivery status update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_date** | **str** | The date and time when the order was received by the guest (Local for delivery terminal). | [optional] 
**delivery_status** | [**DeliveryStatusForUpdate**](DeliveryStatusForUpdate.md) | Delivery status. Can be only switched between these three statuses. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.update_delivery_status_request import UpdateDeliveryStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeliveryStatusRequest from a JSON string
update_delivery_status_request_instance = UpdateDeliveryStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDeliveryStatusRequest.to_json())

# convert the object into a dict
update_delivery_status_request_dict = update_delivery_status_request_instance.to_dict()
# create an instance of UpdateDeliveryStatusRequest from a dict
update_delivery_status_request_from_dict = UpdateDeliveryStatusRequest.from_dict(update_delivery_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


