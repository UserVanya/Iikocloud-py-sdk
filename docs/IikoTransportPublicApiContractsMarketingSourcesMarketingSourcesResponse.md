# IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse

Response to request for marketing sources by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**marketing_sources** | [**List[IikoTransportPublicApiContractsMarketingSourcesMarketingSource]**](IikoTransportPublicApiContractsMarketingSourcesMarketingSource.md) | List of marketing sources. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_marketing_sources_marketing_sources_response import IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse from a JSON string
iiko_transport_public_api_contracts_marketing_sources_marketing_sources_response_instance = IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_marketing_sources_marketing_sources_response_dict = iiko_transport_public_api_contracts_marketing_sources_marketing_sources_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse from a dict
iiko_transport_public_api_contracts_marketing_sources_marketing_sources_response_from_dict = IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse.from_dict(iiko_transport_public_api_contracts_marketing_sources_marketing_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


