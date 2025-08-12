# TransportDeliveriesRequestCancelOrderRequest

Request for cancel the order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**moved_order_id** | **str** | Fill this field with id of the new order if current order has been moved to the new RMS/terminal group. | [optional] 
**cancel_cause_id** | **str** | Cancel order dictionary item id.   &gt; Allowed from version &#x60;7.7.1&#x60;. | [optional] 
**cancel_comment** | **str** | Comment to the delivery cancellation.   &gt; Allowed from version &#x60;8.7.6&#x60;. | [optional] 
**removal_type_id** | **str** | Removal type (for delete printed order items).   &gt; Allowed from version &#x60;7.7.1&#x60;. | [optional] 
**removal_comment** | **str** | Comment to the charge-off.   &gt; Allowed from version &#x60;8.7.6&#x60;. | [optional] 
**user_id_for_writeoff** | **str** | User for writeoff (for delete printed order items).   &gt; Allowed from version &#x60;7.7.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_cancel_order_request import TransportDeliveriesRequestCancelOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCancelOrderRequest from a JSON string
transport_deliveries_request_cancel_order_request_instance = TransportDeliveriesRequestCancelOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCancelOrderRequest.to_json())

# convert the object into a dict
transport_deliveries_request_cancel_order_request_dict = transport_deliveries_request_cancel_order_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestCancelOrderRequest from a dict
transport_deliveries_request_cancel_order_request_from_dict = TransportDeliveriesRequestCancelOrderRequest.from_dict(transport_deliveries_request_cancel_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


