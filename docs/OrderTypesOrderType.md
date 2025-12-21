# OrderTypesOrderType

Order type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Order type ID in RMS. | 
**name** | **str** | Order type name. | 
**order_service_type** | [**OrderTypesOrderServiceType**](OrderTypesOrderServiceType.md) | Service type. | 
**is_deleted** | **bool** | IsDeleted attribute of order type. | [optional] 
**external_revision** | **int** | External system revision number. | [optional] 
**is_default** | **bool** | IsDefault attribute of order type. | [optional] 

## Example

```python
from iikocloud_client.models.order_types_order_type import OrderTypesOrderType

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTypesOrderType from a JSON string
order_types_order_type_instance = OrderTypesOrderType.from_json(json)
# print the JSON string representation of the object
print(OrderTypesOrderType.to_json())

# convert the object into a dict
order_types_order_type_dict = order_types_order_type_instance.to_dict()
# create an instance of OrderTypesOrderType from a dict
order_types_order_type_from_dict = OrderTypesOrderType.from_dict(order_types_order_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


