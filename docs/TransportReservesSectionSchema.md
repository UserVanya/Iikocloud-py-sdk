# TransportReservesSectionSchema

Table layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Layout width in px. | 
**height** | **int** | Layout height in px. | 
**mark_elements** | [**List[TransportReservesRestaurantSectionMark]**](TransportReservesRestaurantSectionMark.md) | Collection of restaurant section marks. | 
**table_elements** | [**List[TransportReservesRestaurantSectionTable]**](TransportReservesRestaurantSectionTable.md) | Collection of restaurant section tables. | 
**rectangle_elements** | [**List[TransportReservesRestaurantSectionRectangle]**](TransportReservesRestaurantSectionRectangle.md) | Collection of restaurant section rectangles. | 
**ellipse_elements** | [**List[TransportReservesRestaurantSectionEllipse]**](TransportReservesRestaurantSectionEllipse.md) | Collection of restaurant section ellipses. | 
**revision** | **int** | Last modified time. | 
**is_deleted** | **bool** | Is schema deleted. | 

## Example

```python
from iikocloud_client.models.transport_reserves_section_schema import TransportReservesSectionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesSectionSchema from a JSON string
transport_reserves_section_schema_instance = TransportReservesSectionSchema.from_json(json)
# print the JSON string representation of the object
print(TransportReservesSectionSchema.to_json())

# convert the object into a dict
transport_reserves_section_schema_dict = transport_reserves_section_schema_instance.to_dict()
# create an instance of TransportReservesSectionSchema from a dict
transport_reserves_section_schema_from_dict = TransportReservesSectionSchema.from_dict(transport_reserves_section_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


