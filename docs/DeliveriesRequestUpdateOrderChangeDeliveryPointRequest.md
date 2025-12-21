# DeliveriesRequestUpdateOrderChangeDeliveryPointRequest

Request for change order's delivery point information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**new_delivery_point** | [**DeliveriesRequestCreateOrderDeliveryPoint**](DeliveriesRequestCreateOrderDeliveryPoint.md) | New address of delivery. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_change_delivery_point_request import DeliveriesRequestUpdateOrderChangeDeliveryPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderChangeDeliveryPointRequest from a JSON string
deliveries_request_update_order_change_delivery_point_request_instance = DeliveriesRequestUpdateOrderChangeDeliveryPointRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderChangeDeliveryPointRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_change_delivery_point_request_dict = deliveries_request_update_order_change_delivery_point_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderChangeDeliveryPointRequest from a dict
deliveries_request_update_order_change_delivery_point_request_from_dict = DeliveriesRequestUpdateOrderChangeDeliveryPointRequest.from_dict(deliveries_request_update_order_change_delivery_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


