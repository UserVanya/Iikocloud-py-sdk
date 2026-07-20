# RestaurantSectionTable

Restaurant section table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angle** | **float** | Item&#39;s angle of slope. | 
**height** | **int** | Item&#39;s height in px. | 
**table_id** | **UUID** | Table ID. | 
**width** | **int** | Item&#39;s width in px. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 

## Example

```python
from iikocloud_client.models.restaurant_section_table import RestaurantSectionTable

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantSectionTable from a JSON string
restaurant_section_table_instance = RestaurantSectionTable.from_json(json)
# print the JSON string representation of the object
print(RestaurantSectionTable.to_json())

# convert the object into a dict
restaurant_section_table_dict = restaurant_section_table_instance.to_dict()
# create an instance of RestaurantSectionTable from a dict
restaurant_section_table_from_dict = RestaurantSectionTable.from_dict(restaurant_section_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


