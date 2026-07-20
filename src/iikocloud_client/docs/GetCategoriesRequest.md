# GetCategoriesRequest

Get categories request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.get_categories_request import GetCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoriesRequest from a JSON string
get_categories_request_instance = GetCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(GetCategoriesRequest.to_json())

# convert the object into a dict
get_categories_request_dict = get_categories_request_instance.to_dict()
# create an instance of GetCategoriesRequest from a dict
get_categories_request_from_dict = GetCategoriesRequest.from_dict(get_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


