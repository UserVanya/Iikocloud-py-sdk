# MarketingSourceDefinition

DTO for marketing source in iikoRMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached_sources** | **List[str]** | Attached marketing sources. | 
**external_revision** | **int** | External system revision number. | [optional] 
**id** | **UUID** | Marketing source ID. | 
**is_deleted** | **bool** | IsDeleted attribute of marketing source. | [optional] 
**name** | **str** | Marketing source name. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.marketing_source_definition import MarketingSourceDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingSourceDefinition from a JSON string
marketing_source_definition_instance = MarketingSourceDefinition.from_json(json)
# print the JSON string representation of the object
print(MarketingSourceDefinition.to_json())

# convert the object into a dict
marketing_source_definition_dict = marketing_source_definition_instance.to_dict()
# create an instance of MarketingSourceDefinition from a dict
marketing_source_definition_from_dict = MarketingSourceDefinition.from_dict(marketing_source_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


