# ReservesChangeBanquetOrderItemsRequest

Request to change banquet order items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Banquet ID. | 
**items** | [**List[DeliveriesRequestCreateOrderOrderItem]**](DeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | [optional] 
**combos** | [**List[DeliveriesRequestCreateOrderCombo]**](DeliveriesRequestCreateOrderCombo.md) | Combos. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_change_banquet_order_items_request import ReservesChangeBanquetOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesChangeBanquetOrderItemsRequest from a JSON string
reserves_change_banquet_order_items_request_instance = ReservesChangeBanquetOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesChangeBanquetOrderItemsRequest.to_json())

# convert the object into a dict
reserves_change_banquet_order_items_request_dict = reserves_change_banquet_order_items_request_instance.to_dict()
# create an instance of ReservesChangeBanquetOrderItemsRequest from a dict
reserves_change_banquet_order_items_request_from_dict = ReservesChangeBanquetOrderItemsRequest.from_dict(reserves_change_banquet_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


