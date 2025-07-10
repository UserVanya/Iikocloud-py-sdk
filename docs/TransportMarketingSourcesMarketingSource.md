# TransportMarketingSourcesMarketingSource

DTO for marketing source in iikoRMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Marketing source ID. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**name** | **str** | Marketing source name. | 
**external_revision** | **int** | External system revision number. | [optional] 
**is_deleted** | **bool** | IsDeleted attribute of marketing source. | [optional] 
**attached_sources** | **List[str]** | Attached marketing sources. | 

## Example

```python
from iiko_cloud_client.models.transport_marketing_sources_marketing_source import TransportMarketingSourcesMarketingSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransportMarketingSourcesMarketingSource from a JSON string
transport_marketing_sources_marketing_source_instance = TransportMarketingSourcesMarketingSource.from_json(json)
# print the JSON string representation of the object
print(TransportMarketingSourcesMarketingSource.to_json())

# convert the object into a dict
transport_marketing_sources_marketing_source_dict = transport_marketing_sources_marketing_source_instance.to_dict()
# create an instance of TransportMarketingSourcesMarketingSource from a dict
transport_marketing_sources_marketing_source_from_dict = TransportMarketingSourcesMarketingSource.from_dict(transport_marketing_sources_marketing_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


