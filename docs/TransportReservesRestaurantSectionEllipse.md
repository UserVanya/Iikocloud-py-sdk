# TransportReservesRestaurantSectionEllipse

Restaurant section ellipse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**TransportReservesColor**](TransportReservesColor.md) | Color. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 
**angle** | **float** | Item&#39;s angle of slope. | 
**width** | **int** | Item&#39;s width in px. | 
**height** | **int** | Item&#39;s height in px. | 

## Example

```python
from iiko_cloud_client.models.transport_reserves_restaurant_section_ellipse import TransportReservesRestaurantSectionEllipse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesRestaurantSectionEllipse from a JSON string
transport_reserves_restaurant_section_ellipse_instance = TransportReservesRestaurantSectionEllipse.from_json(json)
# print the JSON string representation of the object
print(TransportReservesRestaurantSectionEllipse.to_json())

# convert the object into a dict
transport_reserves_restaurant_section_ellipse_dict = transport_reserves_restaurant_section_ellipse_instance.to_dict()
# create an instance of TransportReservesRestaurantSectionEllipse from a dict
transport_reserves_restaurant_section_ellipse_from_dict = TransportReservesRestaurantSectionEllipse.from_dict(transport_reserves_restaurant_section_ellipse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


