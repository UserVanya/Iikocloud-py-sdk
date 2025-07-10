# TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest

Request for change order's delivery point information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**new_delivery_point** | [**TransportDeliveriesRequestCreateOrderDeliveryPoint**](TransportDeliveriesRequestCreateOrderDeliveryPoint.md) | New address of delivery. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_delivery_point_request import TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest from a JSON string
transport_deliveries_request_update_order_change_delivery_point_request_instance = TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_delivery_point_request_dict = transport_deliveries_request_update_order_change_delivery_point_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest from a dict
transport_deliveries_request_update_order_change_delivery_point_request_from_dict = TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.from_dict(transport_deliveries_request_update_order_change_delivery_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


