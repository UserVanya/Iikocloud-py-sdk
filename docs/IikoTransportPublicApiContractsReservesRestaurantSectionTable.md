# IikoTransportPublicApiContractsReservesRestaurantSectionTable

Restaurant section table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **UUID** | Table ID. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 
**angle** | **float** | Item&#39;s angle of slope. | 
**width** | **int** | Item&#39;s width in px. | 
**height** | **int** | Item&#39;s height in px. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_restaurant_section_table import IikoTransportPublicApiContractsReservesRestaurantSectionTable

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesRestaurantSectionTable from a JSON string
iiko_transport_public_api_contracts_reserves_restaurant_section_table_instance = IikoTransportPublicApiContractsReservesRestaurantSectionTable.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesRestaurantSectionTable.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_restaurant_section_table_dict = iiko_transport_public_api_contracts_reserves_restaurant_section_table_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesRestaurantSectionTable from a dict
iiko_transport_public_api_contracts_reserves_restaurant_section_table_from_dict = IikoTransportPublicApiContractsReservesRestaurantSectionTable.from_dict(iiko_transport_public_api_contracts_reserves_restaurant_section_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


