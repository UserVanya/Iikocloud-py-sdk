# TransportReservesGetRestaurantSectionsResponse

Response which contains all restaurant sections of specified terminal groups for which banquet/reserve booking are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**restaurant_sections** | [**List[TransportReservesRestaurantSection]**](TransportReservesRestaurantSection.md) | Restaurant sections. | 
**revision** | **int** | Items list revision. | 

## Example

```python
from iikocloud_client.models.transport_reserves_get_restaurant_sections_response import TransportReservesGetRestaurantSectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesGetRestaurantSectionsResponse from a JSON string
transport_reserves_get_restaurant_sections_response_instance = TransportReservesGetRestaurantSectionsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportReservesGetRestaurantSectionsResponse.to_json())

# convert the object into a dict
transport_reserves_get_restaurant_sections_response_dict = transport_reserves_get_restaurant_sections_response_instance.to_dict()
# create an instance of TransportReservesGetRestaurantSectionsResponse from a dict
transport_reserves_get_restaurant_sections_response_from_dict = TransportReservesGetRestaurantSectionsResponse.from_dict(transport_reserves_get_restaurant_sections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


