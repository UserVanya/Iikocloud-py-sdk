# DeliveryOrderResponseItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Quantity. | 
**combo_information** | [**DeliveryOrderResponseComboItemInformation**](DeliveryOrderResponseComboItemInformation.md) | Combo details, if order item is part of combo. | [optional] 
**comment** | **str** | Comment. | [optional] 
**deleted** | [**ItemDeletedInfo**](ItemDeletedInfo.md) | Item deletion details. If filled up, item is deleted. | [optional] 
**size** | [**ProductSize**](ProductSize.md) | Size. | [optional] 
**status** | [**OrderItemStatus**](OrderItemStatus.md) | Item cooking status. | 
**type** | **str** |  | 
**when_printed** | **str** | Printing time (Local for the terminal). | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_item import DeliveryOrderResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseItem from a JSON string
delivery_order_response_item_instance = DeliveryOrderResponseItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseItem.to_json())

# convert the object into a dict
delivery_order_response_item_dict = delivery_order_response_item_instance.to_dict()
# create an instance of DeliveryOrderResponseItem from a dict
delivery_order_response_item_from_dict = DeliveryOrderResponseItem.from_dict(delivery_order_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


