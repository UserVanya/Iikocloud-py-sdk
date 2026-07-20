# GetRestaurantSectionsWorkloadResponse

Response for check restaurant sections workload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**reserves** | [**List[ReserveInWorkload]**](ReserveInWorkload.md) | Banquets/reserves. | 

## Example

```python
from iikocloud_client.models.get_restaurant_sections_workload_response import GetRestaurantSectionsWorkloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRestaurantSectionsWorkloadResponse from a JSON string
get_restaurant_sections_workload_response_instance = GetRestaurantSectionsWorkloadResponse.from_json(json)
# print the JSON string representation of the object
print(GetRestaurantSectionsWorkloadResponse.to_json())

# convert the object into a dict
get_restaurant_sections_workload_response_dict = get_restaurant_sections_workload_response_instance.to_dict()
# create an instance of GetRestaurantSectionsWorkloadResponse from a dict
get_restaurant_sections_workload_response_from_dict = GetRestaurantSectionsWorkloadResponse.from_dict(get_restaurant_sections_workload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


