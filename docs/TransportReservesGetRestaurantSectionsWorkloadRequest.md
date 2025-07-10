# TransportReservesGetRestaurantSectionsWorkloadRequest

Request for check restaurant sections workload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restaurant_section_ids** | **List[str]** | Collection of restaurant section ID.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | 
**date_from** | **str** | Estimated start time (Local for the terminal). Lower limit.                Order details are stored for 90 days. | 
**date_to** | **str** | Estimated start time (Local for the terminal). Upper limit. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_reserves_get_restaurant_sections_workload_request import TransportReservesGetRestaurantSectionsWorkloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesGetRestaurantSectionsWorkloadRequest from a JSON string
transport_reserves_get_restaurant_sections_workload_request_instance = TransportReservesGetRestaurantSectionsWorkloadRequest.from_json(json)
# print the JSON string representation of the object
print(TransportReservesGetRestaurantSectionsWorkloadRequest.to_json())

# convert the object into a dict
transport_reserves_get_restaurant_sections_workload_request_dict = transport_reserves_get_restaurant_sections_workload_request_instance.to_dict()
# create an instance of TransportReservesGetRestaurantSectionsWorkloadRequest from a dict
transport_reserves_get_restaurant_sections_workload_request_from_dict = TransportReservesGetRestaurantSectionsWorkloadRequest.from_dict(transport_reserves_get_restaurant_sections_workload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


