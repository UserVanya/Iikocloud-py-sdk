# DeliveriesRequestAddOrderItemsRequest

Request for add order items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[DeliveriesRequestCreateOrderOrderItem]**](DeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[DeliveriesRequestCreateOrderCombo]**](DeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_add_order_items_request import DeliveriesRequestAddOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestAddOrderItemsRequest from a JSON string
deliveries_request_add_order_items_request_instance = DeliveriesRequestAddOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestAddOrderItemsRequest.to_json())

# convert the object into a dict
deliveries_request_add_order_items_request_dict = deliveries_request_add_order_items_request_instance.to_dict()
# create an instance of DeliveriesRequestAddOrderItemsRequest from a dict
deliveries_request_add_order_items_request_from_dict = DeliveriesRequestAddOrderItemsRequest.from_dict(deliveries_request_add_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


