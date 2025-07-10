# TransportReservesAddOrderItemsToBanquetRequest

Request for add order items to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserve_id** | **str** | Banquet ID. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[TransportDeliveriesRequestCreateOrderCombo]**](TransportDeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_reserves_add_order_items_to_banquet_request import TransportReservesAddOrderItemsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesAddOrderItemsToBanquetRequest from a JSON string
transport_reserves_add_order_items_to_banquet_request_instance = TransportReservesAddOrderItemsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(TransportReservesAddOrderItemsToBanquetRequest.to_json())

# convert the object into a dict
transport_reserves_add_order_items_to_banquet_request_dict = transport_reserves_add_order_items_to_banquet_request_instance.to_dict()
# create an instance of TransportReservesAddOrderItemsToBanquetRequest from a dict
transport_reserves_add_order_items_to_banquet_request_from_dict = TransportReservesAddOrderItemsToBanquetRequest.from_dict(transport_reserves_add_order_items_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


