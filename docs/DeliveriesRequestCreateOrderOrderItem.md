# DeliveriesRequestCreateOrderOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | **float** | Quantity. | 
**product_size_id** | **str** | Size ID. Required if a stock list item has a size scale. | [optional] 
**combo_information** | [**DeliveriesRequestCreateOrderComboItemInformation**](DeliveriesRequestCreateOrderComboItemInformation.md) | Combo details if combo includes order item. | [optional] 
**comment** | **str** | Comment. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_order_item import DeliveriesRequestCreateOrderOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderOrderItem from a JSON string
deliveries_request_create_order_order_item_instance = DeliveriesRequestCreateOrderOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderOrderItem.to_json())

# convert the object into a dict
deliveries_request_create_order_order_item_dict = deliveries_request_create_order_order_item_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderOrderItem from a dict
deliveries_request_create_order_order_item_from_dict = DeliveriesRequestCreateOrderOrderItem.from_dict(deliveries_request_create_order_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


