# TipsTypeDefinition

Tips type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Tips type ID.                Can be obtained by &#x60;/api/1/tips_types&#x60; operation. | 
**name** | **str** | Tips type name. | 
**order_service_types** | [**List[OrderTypeServiceType]**](OrderTypeServiceType.md) | Supported order service types. | 
**organization_ids** | **List[UUID]** | Supported organizations IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payment_types_ids** | **List[UUID]** | Supported payment types IDs. | 

## Example

```python
from iikocloud_client.models.tips_type_definition import TipsTypeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TipsTypeDefinition from a JSON string
tips_type_definition_instance = TipsTypeDefinition.from_json(json)
# print the JSON string representation of the object
print(TipsTypeDefinition.to_json())

# convert the object into a dict
tips_type_definition_dict = tips_type_definition_instance.to_dict()
# create an instance of TipsTypeDefinition from a dict
tips_type_definition_from_dict = TipsTypeDefinition.from_dict(tips_type_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


