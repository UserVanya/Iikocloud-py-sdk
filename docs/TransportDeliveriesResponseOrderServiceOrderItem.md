# TransportDeliveriesResponseOrderServiceOrderItem

Order item: service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**TransportDeliveriesResponseOrderProduct**](TransportDeliveriesResponseOrderProduct.md) | Item. | 
**cost** | **float** | Total cost per item without tax, discounts/surcharges. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_service_order_item import TransportDeliveriesResponseOrderServiceOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderServiceOrderItem from a JSON string
transport_deliveries_response_order_service_order_item_instance = TransportDeliveriesResponseOrderServiceOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderServiceOrderItem.to_json())

# convert the object into a dict
transport_deliveries_response_order_service_order_item_dict = transport_deliveries_response_order_service_order_item_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderServiceOrderItem from a dict
transport_deliveries_response_order_service_order_item_from_dict = TransportDeliveriesResponseOrderServiceOrderItem.from_dict(transport_deliveries_response_order_service_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


