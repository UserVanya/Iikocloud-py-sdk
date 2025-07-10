# TransportMarketingSourcesMarketingSourcesRequest

Request for marketing sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations IDs which marketing sources have to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iiko_cloud_client.models.transport_marketing_sources_marketing_sources_request import TransportMarketingSourcesMarketingSourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportMarketingSourcesMarketingSourcesRequest from a JSON string
transport_marketing_sources_marketing_sources_request_instance = TransportMarketingSourcesMarketingSourcesRequest.from_json(json)
# print the JSON string representation of the object
print(TransportMarketingSourcesMarketingSourcesRequest.to_json())

# convert the object into a dict
transport_marketing_sources_marketing_sources_request_dict = transport_marketing_sources_marketing_sources_request_instance.to_dict()
# create an instance of TransportMarketingSourcesMarketingSourcesRequest from a dict
transport_marketing_sources_marketing_sources_request_from_dict = TransportMarketingSourcesMarketingSourcesRequest.from_dict(transport_marketing_sources_marketing_sources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


