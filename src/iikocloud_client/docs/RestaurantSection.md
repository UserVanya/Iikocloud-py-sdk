# RestaurantSection

Restaurant section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Restaurant section ID. | 
**name** | **str** | Name. | 
**var_schema** | [**SectionSchema**](SectionSchema.md) | Table layout. | [optional] 
**tables** | [**List[Table]**](Table.md) | Tables. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.restaurant_section import RestaurantSection

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantSection from a JSON string
restaurant_section_instance = RestaurantSection.from_json(json)
# print the JSON string representation of the object
print(RestaurantSection.to_json())

# convert the object into a dict
restaurant_section_dict = restaurant_section_instance.to_dict()
# create an instance of RestaurantSection from a dict
restaurant_section_from_dict = RestaurantSection.from_dict(restaurant_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


