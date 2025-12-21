# IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest

Request for get all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_ids** | **List[UUID]** | Collection of terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**return_schema** | **bool** | Indicates whether table layout information should be returned... | [optional] 
**revision** | **int** | Last modified time after. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request import IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest from a JSON string
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request_instance = IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request_dict = iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest from a dict
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request_from_dict = IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest.from_dict(iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


