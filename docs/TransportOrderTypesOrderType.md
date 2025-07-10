# TransportOrderTypesOrderType

Order type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order type ID in RMS. | 
**name** | **str** | Order type name. | 
**order_service_type** | [**TransportOrderTypesOrderServiceType**](TransportOrderTypesOrderServiceType.md) | Service type. | 
**is_deleted** | **bool** | IsDeleted attribute of order type. | [optional] 
**external_revision** | **int** | External system revision number. | [optional] 
**is_default** | **bool** | IsDefault attribute of order type. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_order_types_order_type import TransportOrderTypesOrderType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrderTypesOrderType from a JSON string
transport_order_types_order_type_instance = TransportOrderTypesOrderType.from_json(json)
# print the JSON string representation of the object
print(TransportOrderTypesOrderType.to_json())

# convert the object into a dict
transport_order_types_order_type_dict = transport_order_types_order_type_instance.to_dict()
# create an instance of TransportOrderTypesOrderType from a dict
transport_order_types_order_type_from_dict = TransportOrderTypesOrderType.from_dict(transport_order_types_order_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


