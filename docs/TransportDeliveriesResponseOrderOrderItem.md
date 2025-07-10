# TransportDeliveriesResponseOrderOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | [**TransportDeliveriesResponseOrderOrderItemStatus**](TransportDeliveriesResponseOrderOrderItemStatus.md) | Item cooking status. | 
**deleted** | [**TransportDeliveriesResponseOrderItemDeletedInfo**](TransportDeliveriesResponseOrderItemDeletedInfo.md) | Item deletion details. If filled up, item is deleted. | [optional] 
**amount** | **float** | Quantity. | 
**comment** | **str** | Comment. | [optional] 
**when_printed** | **str** | Printing time (Local for the terminal). | [optional] 
**size** | [**TransportDeliveriesResponseOrderProductSize**](TransportDeliveriesResponseOrderProductSize.md) | Size. | [optional] 
**combo_information** | [**TransportDeliveriesResponseOrderComboItemInformation**](TransportDeliveriesResponseOrderComboItemInformation.md) | Combo details, if order item is part of combo. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_order_item import TransportDeliveriesResponseOrderOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderOrderItem from a JSON string
transport_deliveries_response_order_order_item_instance = TransportDeliveriesResponseOrderOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderOrderItem.to_json())

# convert the object into a dict
transport_deliveries_response_order_order_item_dict = transport_deliveries_response_order_order_item_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderOrderItem from a dict
transport_deliveries_response_order_order_item_from_dict = TransportDeliveriesResponseOrderOrderItem.from_dict(transport_deliveries_response_order_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


