# ReservesSectionSchema

Table layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Layout width in px. | 
**height** | **int** | Layout height in px. | 
**mark_elements** | [**List[ReservesRestaurantSectionMark]**](ReservesRestaurantSectionMark.md) | Collection of restaurant section marks. | 
**table_elements** | [**List[ReservesRestaurantSectionTable]**](ReservesRestaurantSectionTable.md) | Collection of restaurant section tables. | 
**rectangle_elements** | [**List[ReservesRestaurantSectionRectangle]**](ReservesRestaurantSectionRectangle.md) | Collection of restaurant section rectangles. | 
**ellipse_elements** | [**List[ReservesRestaurantSectionEllipse]**](ReservesRestaurantSectionEllipse.md) | Collection of restaurant section ellipses. | 
**revision** | **int** | Last modified time. | 
**is_deleted** | **bool** | Is schema deleted. | 

## Example

```python
from iikocloud_client.models.reserves_section_schema import ReservesSectionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesSectionSchema from a JSON string
reserves_section_schema_instance = ReservesSectionSchema.from_json(json)
# print the JSON string representation of the object
print(ReservesSectionSchema.to_json())

# convert the object into a dict
reserves_section_schema_dict = reserves_section_schema_instance.to_dict()
# create an instance of ReservesSectionSchema from a dict
reserves_section_schema_from_dict = ReservesSectionSchema.from_dict(reserves_section_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


