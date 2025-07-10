# TransportDeliveriesRequestAddOrderItemsRequest

Request for add order items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[TransportDeliveriesRequestCreateOrderCombo]**](TransportDeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_add_order_items_request import TransportDeliveriesRequestAddOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestAddOrderItemsRequest from a JSON string
transport_deliveries_request_add_order_items_request_instance = TransportDeliveriesRequestAddOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestAddOrderItemsRequest.to_json())

# convert the object into a dict
transport_deliveries_request_add_order_items_request_dict = transport_deliveries_request_add_order_items_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestAddOrderItemsRequest from a dict
transport_deliveries_request_add_order_items_request_from_dict = TransportDeliveriesRequestAddOrderItemsRequest.from_dict(transport_deliveries_request_add_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


