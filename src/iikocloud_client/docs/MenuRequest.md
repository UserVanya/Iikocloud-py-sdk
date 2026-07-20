# MenuRequest

Request for menu by id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_mode** | **bool** | Async Mode. | [optional] 
**external_menu_id** | **str** | External menu id                Can be obtained by &#x60;api/2/menu&#x60; operation. | 
**language** | **str** | Language of the external menu. | [optional] 
**organization_ids** | **List[UUID]** | Organization IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**price_category_id** | **str** | Price category id.                Can be obtained by &#x60;api/2/menu&#x60; operation. | [optional] 
**start_revision** | **int** | Start revision. | [optional] 
**version** | **int** | Version of the result data model. | [optional] 

## Example

```python
from iikocloud_client.models.menu_request import MenuRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MenuRequest from a JSON string
menu_request_instance = MenuRequest.from_json(json)
# print the JSON string representation of the object
print(MenuRequest.to_json())

# convert the object into a dict
menu_request_dict = menu_request_instance.to_dict()
# create an instance of MenuRequest from a dict
menu_request_from_dict = MenuRequest.from_dict(menu_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


