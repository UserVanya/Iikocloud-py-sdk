# DeliveriesResponseOrderOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | [**DeliveriesResponseOrderOrderItemStatus**](DeliveriesResponseOrderOrderItemStatus.md) | Item cooking status. | 
**deleted** | [**DeliveriesResponseOrderItemDeletedInfo**](DeliveriesResponseOrderItemDeletedInfo.md) | Item deletion details. If filled up, item is deleted. | [optional] 
**amount** | **float** | Quantity. | 
**comment** | **str** | Comment. | [optional] 
**when_printed** | **str** | Printing time (Local for the terminal). | [optional] 
**size** | [**DeliveriesResponseOrderProductSize**](DeliveriesResponseOrderProductSize.md) | Size. | [optional] 
**combo_information** | [**DeliveriesResponseOrderComboItemInformation**](DeliveriesResponseOrderComboItemInformation.md) | Combo details, if order item is part of combo. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_order_item import DeliveriesResponseOrderOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderOrderItem from a JSON string
deliveries_response_order_order_item_instance = DeliveriesResponseOrderOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderOrderItem.to_json())

# convert the object into a dict
deliveries_response_order_order_item_dict = deliveries_response_order_order_item_instance.to_dict()
# create an instance of DeliveriesResponseOrderOrderItem from a dict
deliveries_response_order_order_item_from_dict = DeliveriesResponseOrderOrderItem.from_dict(deliveries_response_order_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


