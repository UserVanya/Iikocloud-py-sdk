# ReservesAddOrderItemsToBanquetRequest

Request for add order items to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserve_id** | **str** | Banquet ID. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[DeliveriesRequestCreateOrderOrderItem]**](DeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[DeliveriesRequestCreateOrderCombo]**](DeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_add_order_items_to_banquet_request import ReservesAddOrderItemsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesAddOrderItemsToBanquetRequest from a JSON string
reserves_add_order_items_to_banquet_request_instance = ReservesAddOrderItemsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesAddOrderItemsToBanquetRequest.to_json())

# convert the object into a dict
reserves_add_order_items_to_banquet_request_dict = reserves_add_order_items_to_banquet_request_instance.to_dict()
# create an instance of ReservesAddOrderItemsToBanquetRequest from a dict
reserves_add_order_items_to_banquet_request_from_dict = ReservesAddOrderItemsToBanquetRequest.from_dict(reserves_add_order_items_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


