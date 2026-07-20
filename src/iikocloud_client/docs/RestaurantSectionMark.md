# RestaurantSectionMark

Restaurant section mark.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angle** | **float** | Item&#39;s angle of slope. | 
**color** | [**Color**](Color.md) | Color. | 
**font** | [**Font**](Font.md) | Font. | 
**height** | **int** | Item&#39;s height in px. | 
**text** | **str** | Text. | 
**width** | **int** | Item&#39;s width in px. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 

## Example

```python
from iikocloud_client.models.restaurant_section_mark import RestaurantSectionMark

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantSectionMark from a JSON string
restaurant_section_mark_instance = RestaurantSectionMark.from_json(json)
# print the JSON string representation of the object
print(RestaurantSectionMark.to_json())

# convert the object into a dict
restaurant_section_mark_dict = restaurant_section_mark_instance.to_dict()
# create an instance of RestaurantSectionMark from a dict
restaurant_section_mark_from_dict = RestaurantSectionMark.from_dict(restaurant_section_mark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


