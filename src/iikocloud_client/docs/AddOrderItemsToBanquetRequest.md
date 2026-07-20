# AddOrderItemsToBanquetRequest

Request for add order items to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combos** | [**List[Combo]**](Combo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Banquet ID. | 

## Example

```python
from iikocloud_client.models.add_order_items_to_banquet_request import AddOrderItemsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrderItemsToBanquetRequest from a JSON string
add_order_items_to_banquet_request_instance = AddOrderItemsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(AddOrderItemsToBanquetRequest.to_json())

# convert the object into a dict
add_order_items_to_banquet_request_dict = add_order_items_to_banquet_request_instance.to_dict()
# create an instance of AddOrderItemsToBanquetRequest from a dict
add_order_items_to_banquet_request_from_dict = AddOrderItemsToBanquetRequest.from_dict(add_order_items_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


