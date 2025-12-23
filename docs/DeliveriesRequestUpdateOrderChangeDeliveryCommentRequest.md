# DeliveriesRequestUpdateOrderChangeDeliveryCommentRequest

Request for change delivery comment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. | 
**order_id** | **str** | Order ID. | 
**comment** | **str** | New delivery comment. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_change_delivery_comment_request import DeliveriesRequestUpdateOrderChangeDeliveryCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderChangeDeliveryCommentRequest from a JSON string
deliveries_request_update_order_change_delivery_comment_request_instance = DeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_change_delivery_comment_request_dict = deliveries_request_update_order_change_delivery_comment_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderChangeDeliveryCommentRequest from a dict
deliveries_request_update_order_change_delivery_comment_request_from_dict = DeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.from_dict(deliveries_request_update_order_change_delivery_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


