# ReservesRestaurantSectionEllipse

Restaurant section ellipse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**ReservesColor**](ReservesColor.md) | Color. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 
**angle** | **float** | Item&#39;s angle of slope. | 
**width** | **int** | Item&#39;s width in px. | 
**height** | **int** | Item&#39;s height in px. | 

## Example

```python
from iikocloud_client.models.reserves_restaurant_section_ellipse import ReservesRestaurantSectionEllipse

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesRestaurantSectionEllipse from a JSON string
reserves_restaurant_section_ellipse_instance = ReservesRestaurantSectionEllipse.from_json(json)
# print the JSON string representation of the object
print(ReservesRestaurantSectionEllipse.to_json())

# convert the object into a dict
reserves_restaurant_section_ellipse_dict = reserves_restaurant_section_ellipse_instance.to_dict()
# create an instance of ReservesRestaurantSectionEllipse from a dict
reserves_restaurant_section_ellipse_from_dict = ReservesRestaurantSectionEllipse.from_dict(reserves_restaurant_section_ellipse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


