# MarketingSourcesResponse

Response to request for marketing sources by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**marketing_sources** | [**List[MarketingSourceDefinition]**](MarketingSourceDefinition.md) | List of marketing sources. | 

## Example

```python
from iikocloud_client.models.marketing_sources_response import MarketingSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingSourcesResponse from a JSON string
marketing_sources_response_instance = MarketingSourcesResponse.from_json(json)
# print the JSON string representation of the object
print(MarketingSourcesResponse.to_json())

# convert the object into a dict
marketing_sources_response_dict = marketing_sources_response_instance.to_dict()
# create an instance of MarketingSourcesResponse from a dict
marketing_sources_response_from_dict = MarketingSourcesResponse.from_dict(marketing_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


