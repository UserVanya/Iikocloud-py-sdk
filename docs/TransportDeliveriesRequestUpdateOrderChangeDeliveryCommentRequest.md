# TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest

Request for change delivery comment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. | 
**order_id** | **str** | Order ID. | 
**comment** | **str** | New delivery comment. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_delivery_comment_request import TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest from a JSON string
transport_deliveries_request_update_order_change_delivery_comment_request_instance = TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_delivery_comment_request_dict = transport_deliveries_request_update_order_change_delivery_comment_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest from a dict
transport_deliveries_request_update_order_change_delivery_comment_request_from_dict = TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.from_dict(transport_deliveries_request_update_order_change_delivery_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


