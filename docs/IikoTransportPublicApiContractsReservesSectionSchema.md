# IikoTransportPublicApiContractsReservesSectionSchema

Table layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Layout width in px. | 
**height** | **int** | Layout height in px. | 
**mark_elements** | [**List[IikoTransportPublicApiContractsReservesRestaurantSectionMark]**](IikoTransportPublicApiContractsReservesRestaurantSectionMark.md) | Collection of restaurant section marks. | 
**table_elements** | [**List[IikoTransportPublicApiContractsReservesRestaurantSectionTable]**](IikoTransportPublicApiContractsReservesRestaurantSectionTable.md) | Collection of restaurant section tables. | 
**rectangle_elements** | [**List[IikoTransportPublicApiContractsReservesRestaurantSectionRectangle]**](IikoTransportPublicApiContractsReservesRestaurantSectionRectangle.md) | Collection of restaurant section rectangles. | 
**ellipse_elements** | [**List[IikoTransportPublicApiContractsReservesRestaurantSectionEllipse]**](IikoTransportPublicApiContractsReservesRestaurantSectionEllipse.md) | Collection of restaurant section ellipses. | 
**revision** | **int** | Last modified time. | 
**is_deleted** | **bool** | Is schema deleted. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_section_schema import IikoTransportPublicApiContractsReservesSectionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesSectionSchema from a JSON string
iiko_transport_public_api_contracts_reserves_section_schema_instance = IikoTransportPublicApiContractsReservesSectionSchema.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesSectionSchema.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_section_schema_dict = iiko_transport_public_api_contracts_reserves_section_schema_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesSectionSchema from a dict
iiko_transport_public_api_contracts_reserves_section_schema_from_dict = IikoTransportPublicApiContractsReservesSectionSchema.from_dict(iiko_transport_public_api_contracts_reserves_section_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


