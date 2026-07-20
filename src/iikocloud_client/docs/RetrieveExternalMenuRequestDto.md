# RetrieveExternalMenuRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_mode** | **bool** | Async Mode. | [optional] [default to False]
**external_menu_id** | **str** | External menu id                Can be obtained by &#x60;api/2/menu&#x60; operation. | 
**language** | **str** | Language of the external menu. | [optional] 
**organization_ids** | **List[UUID]** | Organization IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**price_category_id** | **str** | Price category id.                Can be obtained by &#x60;api/2/menu&#x60; operation. | [optional] 
**start_revision** | **int** | Start revision. | [optional] 
**version** | **int** | Version of the result data model. | [optional] 

## Example

```python
from iikocloud_client.models.retrieve_external_menu_request_dto import RetrieveExternalMenuRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveExternalMenuRequestDto from a JSON string
retrieve_external_menu_request_dto_instance = RetrieveExternalMenuRequestDto.from_json(json)
# print the JSON string representation of the object
print(RetrieveExternalMenuRequestDto.to_json())

# convert the object into a dict
retrieve_external_menu_request_dto_dict = retrieve_external_menu_request_dto_instance.to_dict()
# create an instance of RetrieveExternalMenuRequestDto from a dict
retrieve_external_menu_request_dto_from_dict = RetrieveExternalMenuRequestDto.from_dict(retrieve_external_menu_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


