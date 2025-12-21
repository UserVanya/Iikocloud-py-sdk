# IikoTransportPublicApiContractsReservesRestaurantSection

Restaurant section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Restaurant section ID. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**name** | **str** | Name. | 
**tables** | [**List[IikoTransportPublicApiContractsReservesTable]**](IikoTransportPublicApiContractsReservesTable.md) | Tables. | 
**var_schema** | [**IikoTransportPublicApiContractsReservesSectionSchema**](IikoTransportPublicApiContractsReservesSectionSchema.md) | Table layout. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_restaurant_section import IikoTransportPublicApiContractsReservesRestaurantSection

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesRestaurantSection from a JSON string
iiko_transport_public_api_contracts_reserves_restaurant_section_instance = IikoTransportPublicApiContractsReservesRestaurantSection.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesRestaurantSection.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_restaurant_section_dict = iiko_transport_public_api_contracts_reserves_restaurant_section_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesRestaurantSection from a dict
iiko_transport_public_api_contracts_reserves_restaurant_section_from_dict = IikoTransportPublicApiContractsReservesRestaurantSection.from_dict(iiko_transport_public_api_contracts_reserves_restaurant_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


