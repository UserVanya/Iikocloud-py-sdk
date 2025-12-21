# IikoTransportPublicApiContractsMarketingSourcesMarketingSource

DTO for marketing source in iikoRMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Marketing source ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**name** | **str** | Marketing source name. | 
**external_revision** | **int** | External system revision number. | [optional] 
**is_deleted** | **bool** | IsDeleted attribute of marketing source. | [optional] 
**attached_sources** | **List[str]** | Attached marketing sources. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_marketing_sources_marketing_source import IikoTransportPublicApiContractsMarketingSourcesMarketingSource

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsMarketingSourcesMarketingSource from a JSON string
iiko_transport_public_api_contracts_marketing_sources_marketing_source_instance = IikoTransportPublicApiContractsMarketingSourcesMarketingSource.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsMarketingSourcesMarketingSource.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_marketing_sources_marketing_source_dict = iiko_transport_public_api_contracts_marketing_sources_marketing_source_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsMarketingSourcesMarketingSource from a dict
iiko_transport_public_api_contracts_marketing_sources_marketing_source_from_dict = IikoTransportPublicApiContractsMarketingSourcesMarketingSource.from_dict(iiko_transport_public_api_contracts_marketing_sources_marketing_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


