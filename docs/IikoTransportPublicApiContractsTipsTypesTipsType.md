# IikoTransportPublicApiContractsTipsTypesTipsType

Tips type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Tips type ID.                Can be obtained by &#x60;/tips_types&#x60; operation. | 
**name** | **str** | Tips type name. | 
**organization_ids** | **List[UUID]** | Supported organizations IDs.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_service_types** | [**List[IikoTransportPublicApiContractsOrderTypesOrderServiceType]**](IikoTransportPublicApiContractsOrderTypesOrderServiceType.md) | Supported order service types. | 
**payment_types_ids** | **List[UUID]** | Supported payment types IDs. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_tips_types_tips_type import IikoTransportPublicApiContractsTipsTypesTipsType

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTipsTypesTipsType from a JSON string
iiko_transport_public_api_contracts_tips_types_tips_type_instance = IikoTransportPublicApiContractsTipsTypesTipsType.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTipsTypesTipsType.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_tips_types_tips_type_dict = iiko_transport_public_api_contracts_tips_types_tips_type_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTipsTypesTipsType from a dict
iiko_transport_public_api_contracts_tips_types_tips_type_from_dict = IikoTransportPublicApiContractsTipsTypesTipsType.from_dict(iiko_transport_public_api_contracts_tips_types_tips_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


