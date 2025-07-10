# TransportDeliveriesRequestCreateOrderOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | **float** | Quantity. | 
**product_size_id** | **str** | Size ID. Required if a stock list item has a size scale. | [optional] 
**combo_information** | [**TransportDeliveriesRequestCreateOrderComboItemInformation**](TransportDeliveriesRequestCreateOrderComboItemInformation.md) | Combo details if combo includes order item. | [optional] 
**comment** | **str** | Comment. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_order_item import TransportDeliveriesRequestCreateOrderOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderOrderItem from a JSON string
transport_deliveries_request_create_order_order_item_instance = TransportDeliveriesRequestCreateOrderOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderOrderItem.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_order_item_dict = transport_deliveries_request_create_order_order_item_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderOrderItem from a dict
transport_deliveries_request_create_order_order_item_from_dict = TransportDeliveriesRequestCreateOrderOrderItem.from_dict(transport_deliveries_request_create_order_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


