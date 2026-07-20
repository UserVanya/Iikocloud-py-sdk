# ChangeBanquetOrderItemsRequest

Request to change banquet order items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combos** | [**List[Combo]**](Combo.md) | Combos. | [optional] 
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Banquet ID. | 

## Example

```python
from iikocloud_client.models.change_banquet_order_items_request import ChangeBanquetOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeBanquetOrderItemsRequest from a JSON string
change_banquet_order_items_request_instance = ChangeBanquetOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeBanquetOrderItemsRequest.to_json())

# convert the object into a dict
change_banquet_order_items_request_dict = change_banquet_order_items_request_instance.to_dict()
# create an instance of ChangeBanquetOrderItemsRequest from a dict
change_banquet_order_items_request_from_dict = ChangeBanquetOrderItemsRequest.from_dict(change_banquet_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


