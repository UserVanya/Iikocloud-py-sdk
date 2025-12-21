# IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest

Request for marketing sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which marketing sources have to be returned.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request import IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest from a JSON string
iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request_instance = IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request_dict = iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest from a dict
iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request_from_dict = IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest.from_dict(iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


