# IikoTransportPublicApiContractsReservesRestaurantSectionRectangle

Restaurant section rectangle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**IikoTransportPublicApiContractsReservesColor**](IikoTransportPublicApiContractsReservesColor.md) | Color. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 
**angle** | **float** | Item&#39;s angle of slope. | 
**width** | **int** | Item&#39;s width in px. | 
**height** | **int** | Item&#39;s height in px. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_restaurant_section_rectangle import IikoTransportPublicApiContractsReservesRestaurantSectionRectangle

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesRestaurantSectionRectangle from a JSON string
iiko_transport_public_api_contracts_reserves_restaurant_section_rectangle_instance = IikoTransportPublicApiContractsReservesRestaurantSectionRectangle.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesRestaurantSectionRectangle.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_restaurant_section_rectangle_dict = iiko_transport_public_api_contracts_reserves_restaurant_section_rectangle_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesRestaurantSectionRectangle from a dict
iiko_transport_public_api_contracts_reserves_restaurant_section_rectangle_from_dict = IikoTransportPublicApiContractsReservesRestaurantSectionRectangle.from_dict(iiko_transport_public_api_contracts_reserves_restaurant_section_rectangle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


