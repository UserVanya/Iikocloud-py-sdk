# MarketingSourcesRequest

Request for marketing sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which marketing sources have to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.marketing_sources_request import MarketingSourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingSourcesRequest from a JSON string
marketing_sources_request_instance = MarketingSourcesRequest.from_json(json)
# print the JSON string representation of the object
print(MarketingSourcesRequest.to_json())

# convert the object into a dict
marketing_sources_request_dict = marketing_sources_request_instance.to_dict()
# create an instance of MarketingSourcesRequest from a dict
marketing_sources_request_from_dict = MarketingSourcesRequest.from_dict(marketing_sources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


