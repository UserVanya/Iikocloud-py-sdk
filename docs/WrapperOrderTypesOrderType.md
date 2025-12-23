# WrapperOrderTypesOrderType

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[OrderTypesOrderType]**](OrderTypesOrderType.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_order_types_order_type import WrapperOrderTypesOrderType

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperOrderTypesOrderType from a JSON string
wrapper_order_types_order_type_instance = WrapperOrderTypesOrderType.from_json(json)
# print the JSON string representation of the object
print(WrapperOrderTypesOrderType.to_json())

# convert the object into a dict
wrapper_order_types_order_type_dict = wrapper_order_types_order_type_instance.to_dict()
# create an instance of WrapperOrderTypesOrderType from a dict
wrapper_order_types_order_type_from_dict = WrapperOrderTypesOrderType.from_dict(wrapper_order_types_order_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


