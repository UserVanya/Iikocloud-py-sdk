# IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse

Response for check restaurant sections workload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**reserves** | [**List[IikoTransportPublicApiContractsReservesReserveInWorkload]**](IikoTransportPublicApiContractsReservesReserveInWorkload.md) | Banquets/reserves. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_response import IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse from a JSON string
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_response_instance = IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_response_dict = iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse from a dict
iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_response_from_dict = IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse.from_dict(iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


