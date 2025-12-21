# IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse

Response which contains all restaurant sections of specified terminal groups for which banquet/reserve booking are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**restaurant_sections** | [**List[IikoTransportPublicApiContractsReservesRestaurantSection]**](IikoTransportPublicApiContractsReservesRestaurantSection.md) | Restaurant sections. | 
**revision** | **int** | Items list revision. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_get_restaurant_sections_response import IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse from a JSON string
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_response_instance = IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_response_dict = iiko_transport_public_api_contracts_reserves_get_restaurant_sections_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse from a dict
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_response_from_dict = IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse.from_dict(iiko_transport_public_api_contracts_reserves_get_restaurant_sections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


