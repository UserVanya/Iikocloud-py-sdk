# TransportReservesGetRestaurantSectionsWorkloadResponse

Response for check restaurant sections workload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**reserves** | [**List[TransportReservesReserveInWorkload]**](TransportReservesReserveInWorkload.md) | Banquets/reserves. | 

## Example

```python
from iikocloud_client.models.transport_reserves_get_restaurant_sections_workload_response import TransportReservesGetRestaurantSectionsWorkloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesGetRestaurantSectionsWorkloadResponse from a JSON string
transport_reserves_get_restaurant_sections_workload_response_instance = TransportReservesGetRestaurantSectionsWorkloadResponse.from_json(json)
# print the JSON string representation of the object
print(TransportReservesGetRestaurantSectionsWorkloadResponse.to_json())

# convert the object into a dict
transport_reserves_get_restaurant_sections_workload_response_dict = transport_reserves_get_restaurant_sections_workload_response_instance.to_dict()
# create an instance of TransportReservesGetRestaurantSectionsWorkloadResponse from a dict
transport_reserves_get_restaurant_sections_workload_response_from_dict = TransportReservesGetRestaurantSectionsWorkloadResponse.from_dict(transport_reserves_get_restaurant_sections_workload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


