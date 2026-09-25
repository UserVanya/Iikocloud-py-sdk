# MenuSectionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MenuSection]**](MenuSection.md) | List of directory entries | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of directory entries | [optional] 

## Example

```python
from iikocloud_client.models.menu_section_list_response import MenuSectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSectionListResponse from a JSON string
menu_section_list_response_instance = MenuSectionListResponse.from_json(json)
# print the JSON string representation of the object
print(MenuSectionListResponse.to_json())

# convert the object into a dict
menu_section_list_response_dict = menu_section_list_response_instance.to_dict()
# create an instance of MenuSectionListResponse from a dict
menu_section_list_response_from_dict = MenuSectionListResponse.from_dict(menu_section_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


