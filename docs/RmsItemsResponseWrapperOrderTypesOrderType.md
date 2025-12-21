# RmsItemsResponseWrapperOrderTypesOrderType

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsOrderTypesOrderType]**](IikoTransportPublicApiContractsOrderTypesOrderType.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.rms_items_response_wrapper_order_types_order_type import RmsItemsResponseWrapperOrderTypesOrderType

# TODO update the JSON string below
json = "{}"
# create an instance of RmsItemsResponseWrapperOrderTypesOrderType from a JSON string
rms_items_response_wrapper_order_types_order_type_instance = RmsItemsResponseWrapperOrderTypesOrderType.from_json(json)
# print the JSON string representation of the object
print(RmsItemsResponseWrapperOrderTypesOrderType.to_json())

# convert the object into a dict
rms_items_response_wrapper_order_types_order_type_dict = rms_items_response_wrapper_order_types_order_type_instance.to_dict()
# create an instance of RmsItemsResponseWrapperOrderTypesOrderType from a dict
rms_items_response_wrapper_order_types_order_type_from_dict = RmsItemsResponseWrapperOrderTypesOrderType.from_dict(rms_items_response_wrapper_order_types_order_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


