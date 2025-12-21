# ReservesRestaurantSectionMark

Restaurant section mark.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text. | 
**font** | [**ReservesFont**](ReservesFont.md) | Font. | 
**color** | [**ReservesColor**](ReservesColor.md) | Color. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 
**angle** | **float** | Item&#39;s angle of slope. | 
**width** | **int** | Item&#39;s width in px. | 
**height** | **int** | Item&#39;s height in px. | 

## Example

```python
from iikocloud_client.models.reserves_restaurant_section_mark import ReservesRestaurantSectionMark

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesRestaurantSectionMark from a JSON string
reserves_restaurant_section_mark_instance = ReservesRestaurantSectionMark.from_json(json)
# print the JSON string representation of the object
print(ReservesRestaurantSectionMark.to_json())

# convert the object into a dict
reserves_restaurant_section_mark_dict = reserves_restaurant_section_mark_instance.to_dict()
# create an instance of ReservesRestaurantSectionMark from a dict
reserves_restaurant_section_mark_from_dict = ReservesRestaurantSectionMark.from_dict(reserves_restaurant_section_mark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


