# TransportDeliveriesResponseOrderTipsType

The tips type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tips type ID.                Can be obtained by &#x60;/api/1/tips_types&#x60; operation. | 
**name** | **str** | Tips type name. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_tips_type import TransportDeliveriesResponseOrderTipsType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderTipsType from a JSON string
transport_deliveries_response_order_tips_type_instance = TransportDeliveriesResponseOrderTipsType.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderTipsType.to_json())

# convert the object into a dict
transport_deliveries_response_order_tips_type_dict = transport_deliveries_response_order_tips_type_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderTipsType from a dict
transport_deliveries_response_order_tips_type_from_dict = TransportDeliveriesResponseOrderTipsType.from_dict(transport_deliveries_response_order_tips_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


