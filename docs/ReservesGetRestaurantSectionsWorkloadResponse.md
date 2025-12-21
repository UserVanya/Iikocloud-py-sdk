# ReservesGetRestaurantSectionsWorkloadResponse

Response for check restaurant sections workload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**reserves** | [**List[ReservesReserveInWorkload]**](ReservesReserveInWorkload.md) | Banquets/reserves. | 

## Example

```python
from iikocloud_client.models.reserves_get_restaurant_sections_workload_response import ReservesGetRestaurantSectionsWorkloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesGetRestaurantSectionsWorkloadResponse from a JSON string
reserves_get_restaurant_sections_workload_response_instance = ReservesGetRestaurantSectionsWorkloadResponse.from_json(json)
# print the JSON string representation of the object
print(ReservesGetRestaurantSectionsWorkloadResponse.to_json())

# convert the object into a dict
reserves_get_restaurant_sections_workload_response_dict = reserves_get_restaurant_sections_workload_response_instance.to_dict()
# create an instance of ReservesGetRestaurantSectionsWorkloadResponse from a dict
reserves_get_restaurant_sections_workload_response_from_dict = ReservesGetRestaurantSectionsWorkloadResponse.from_dict(reserves_get_restaurant_sections_workload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


