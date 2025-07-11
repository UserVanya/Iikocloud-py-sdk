# TransportDeliveriesResponseOrderOrderType

Order type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**order_service_type** | [**TransportDeliveriesCommonOrderServiceType**](TransportDeliveriesCommonOrderServiceType.md) | Order type. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_order_type import TransportDeliveriesResponseOrderOrderType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderOrderType from a JSON string
transport_deliveries_response_order_order_type_instance = TransportDeliveriesResponseOrderOrderType.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderOrderType.to_json())

# convert the object into a dict
transport_deliveries_response_order_order_type_dict = transport_deliveries_response_order_order_type_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderOrderType from a dict
transport_deliveries_response_order_order_type_from_dict = TransportDeliveriesResponseOrderOrderType.from_dict(transport_deliveries_response_order_order_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


