# ReservesGetRestaurantSectionsResponse

Response which contains all restaurant sections of specified terminal groups for which banquet/reserve booking are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**restaurant_sections** | [**List[ReservesRestaurantSection]**](ReservesRestaurantSection.md) | Restaurant sections. | 
**revision** | **int** | Items list revision. | 

## Example

```python
from iikocloud_client.models.reserves_get_restaurant_sections_response import ReservesGetRestaurantSectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesGetRestaurantSectionsResponse from a JSON string
reserves_get_restaurant_sections_response_instance = ReservesGetRestaurantSectionsResponse.from_json(json)
# print the JSON string representation of the object
print(ReservesGetRestaurantSectionsResponse.to_json())

# convert the object into a dict
reserves_get_restaurant_sections_response_dict = reserves_get_restaurant_sections_response_instance.to_dict()
# create an instance of ReservesGetRestaurantSectionsResponse from a dict
reserves_get_restaurant_sections_response_from_dict = ReservesGetRestaurantSectionsResponse.from_dict(reserves_get_restaurant_sections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


