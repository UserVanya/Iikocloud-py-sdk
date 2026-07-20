# DeliveryOrderCreateItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Quantity. | 
**combo_information** | [**DeliveryOrderCreateComboItemInformation**](DeliveryOrderCreateComboItemInformation.md) | Combo details if combo includes order item. | [optional] 
**comment** | **str** | Comment. | [optional] 
**product_size_id** | **UUID** | Size ID. Required if a stock list item has a size scale. | [optional] 
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.delivery_order_create_item import DeliveryOrderCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateItem from a JSON string
delivery_order_create_item_instance = DeliveryOrderCreateItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateItem.to_json())

# convert the object into a dict
delivery_order_create_item_dict = delivery_order_create_item_instance.to_dict()
# create an instance of DeliveryOrderCreateItem from a dict
delivery_order_create_item_from_dict = DeliveryOrderCreateItem.from_dict(delivery_order_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


