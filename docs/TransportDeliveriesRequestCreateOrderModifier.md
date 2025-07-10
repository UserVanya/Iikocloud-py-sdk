# TransportDeliveriesRequestCreateOrderModifier

Modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Modifier item ID.                Can be obtained by &#x60;/api/1/nomenclature&#x60; operation. | 
**amount** | **float** | Quantity. | 
**product_group_id** | **str** | Modifiers group ID (for group modifier). Required for a group modifier.                Can be obtained by &#x60;/api/1/nomenclature&#x60; operation. | [optional] 
**price** | **float** | Unit price. | [optional] 
**position_id** | **str** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_modifier import TransportDeliveriesRequestCreateOrderModifier

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderModifier from a JSON string
transport_deliveries_request_create_order_modifier_instance = TransportDeliveriesRequestCreateOrderModifier.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderModifier.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_modifier_dict = transport_deliveries_request_create_order_modifier_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderModifier from a dict
transport_deliveries_request_create_order_modifier_from_dict = TransportDeliveriesRequestCreateOrderModifier.from_dict(transport_deliveries_request_create_order_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


