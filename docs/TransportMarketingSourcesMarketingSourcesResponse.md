# TransportMarketingSourcesMarketingSourcesResponse

Response to request for marketing sources by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**marketing_sources** | [**List[TransportMarketingSourcesMarketingSource]**](TransportMarketingSourcesMarketingSource.md) | List of marketing sources. | 

## Example

```python
from iikocloud_client.models.transport_marketing_sources_marketing_sources_response import TransportMarketingSourcesMarketingSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportMarketingSourcesMarketingSourcesResponse from a JSON string
transport_marketing_sources_marketing_sources_response_instance = TransportMarketingSourcesMarketingSourcesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportMarketingSourcesMarketingSourcesResponse.to_json())

# convert the object into a dict
transport_marketing_sources_marketing_sources_response_dict = transport_marketing_sources_marketing_sources_response_instance.to_dict()
# create an instance of TransportMarketingSourcesMarketingSourcesResponse from a dict
transport_marketing_sources_marketing_sources_response_from_dict = TransportMarketingSourcesMarketingSourcesResponse.from_dict(transport_marketing_sources_marketing_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


