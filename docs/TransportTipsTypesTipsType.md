# TransportTipsTypesTipsType

Tips type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Tips type ID.                Can be obtained by &#x60;/api/1/tips_types&#x60; operation. | 
**name** | **str** | Tips type name. | 
**organization_ids** | **List[str]** | Supported organizations IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_service_types** | [**List[TransportOrderTypesOrderServiceType]**](TransportOrderTypesOrderServiceType.md) | Supported order service types. | 
**payment_types_ids** | **List[str]** | Supported payment types IDs. | 

## Example

```python
from iiko_cloud_client.models.transport_tips_types_tips_type import TransportTipsTypesTipsType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTipsTypesTipsType from a JSON string
transport_tips_types_tips_type_instance = TransportTipsTypesTipsType.from_json(json)
# print the JSON string representation of the object
print(TransportTipsTypesTipsType.to_json())

# convert the object into a dict
transport_tips_types_tips_type_dict = transport_tips_types_tips_type_instance.to_dict()
# create an instance of TransportTipsTypesTipsType from a dict
transport_tips_types_tips_type_from_dict = TransportTipsTypesTipsType.from_dict(transport_tips_types_tips_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


