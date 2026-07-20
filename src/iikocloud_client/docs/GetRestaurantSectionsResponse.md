# GetRestaurantSectionsResponse

Response which contains all restaurant sections of specified terminal groups for which banquet/reserve booking are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**restaurant_sections** | [**List[RestaurantSection]**](RestaurantSection.md) | Restaurant sections. | 
**revision** | **int** | Items list revision. | 

## Example

```python
from iikocloud_client.models.get_restaurant_sections_response import GetRestaurantSectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRestaurantSectionsResponse from a JSON string
get_restaurant_sections_response_instance = GetRestaurantSectionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRestaurantSectionsResponse.to_json())

# convert the object into a dict
get_restaurant_sections_response_dict = get_restaurant_sections_response_instance.to_dict()
# create an instance of GetRestaurantSectionsResponse from a dict
get_restaurant_sections_response_from_dict = GetRestaurantSectionsResponse.from_dict(get_restaurant_sections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


