# SectionSchema

Table layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ellipse_elements** | [**List[RestaurantSectionEllipse]**](RestaurantSectionEllipse.md) | Collection of restaurant section ellipses. | 
**height** | **int** | Layout height in px. | 
**is_deleted** | **bool** | Is schema deleted. | 
**mark_elements** | [**List[RestaurantSectionMark]**](RestaurantSectionMark.md) | Collection of restaurant section marks. | 
**rectangle_elements** | [**List[RestaurantSectionRectangle]**](RestaurantSectionRectangle.md) | Collection of restaurant section rectangles. | 
**revision** | **int** | Last modified time. | 
**table_elements** | [**List[RestaurantSectionTable]**](RestaurantSectionTable.md) | Collection of restaurant section tables. | 
**width** | **int** | Layout width in px. | 

## Example

```python
from iikocloud_client.models.section_schema import SectionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SectionSchema from a JSON string
section_schema_instance = SectionSchema.from_json(json)
# print the JSON string representation of the object
print(SectionSchema.to_json())

# convert the object into a dict
section_schema_dict = section_schema_instance.to_dict()
# create an instance of SectionSchema from a dict
section_schema_from_dict = SectionSchema.from_dict(section_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


