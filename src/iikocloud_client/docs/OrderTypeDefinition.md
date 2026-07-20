# OrderTypeDefinition

Order type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_revision** | **int** | External system revision number. | [optional] 
**id** | **UUID** | Order type ID in RMS. | 
**is_default** | **bool** | IsDefault attribute of order type. | [optional] 
**is_deleted** | **bool** | IsDeleted attribute of order type. | [optional] 
**name** | **str** | Order type name. | 
**order_service_type** | [**OrderTypeServiceType**](OrderTypeServiceType.md) | Service type. | 

## Example

```python
from iikocloud_client.models.order_type_definition import OrderTypeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTypeDefinition from a JSON string
order_type_definition_instance = OrderTypeDefinition.from_json(json)
# print the JSON string representation of the object
print(OrderTypeDefinition.to_json())

# convert the object into a dict
order_type_definition_dict = order_type_definition_instance.to_dict()
# create an instance of OrderTypeDefinition from a dict
order_type_definition_from_dict = OrderTypeDefinition.from_dict(order_type_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


