# MarketingSourcesMarketingSourcesResponse

Response to request for marketing sources by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**marketing_sources** | [**List[MarketingSourcesMarketingSource]**](MarketingSourcesMarketingSource.md) | List of marketing sources. | 

## Example

```python
from iikocloud_client.models.marketing_sources_marketing_sources_response import MarketingSourcesMarketingSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingSourcesMarketingSourcesResponse from a JSON string
marketing_sources_marketing_sources_response_instance = MarketingSourcesMarketingSourcesResponse.from_json(json)
# print the JSON string representation of the object
print(MarketingSourcesMarketingSourcesResponse.to_json())

# convert the object into a dict
marketing_sources_marketing_sources_response_dict = marketing_sources_marketing_sources_response_instance.to_dict()
# create an instance of MarketingSourcesMarketingSourcesResponse from a dict
marketing_sources_marketing_sources_response_from_dict = MarketingSourcesMarketingSourcesResponse.from_dict(marketing_sources_marketing_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


