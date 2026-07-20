# GetRestaurantSectionsRequest

Request for get all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_schema** | **bool** | Indicates whether table layout information should be returned... | [optional] 
**revision** | **int** | Last modified time after. | [optional] 
**terminal_group_ids** | **List[UUID]** | Collection of terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_restaurant_sections_request import GetRestaurantSectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRestaurantSectionsRequest from a JSON string
get_restaurant_sections_request_instance = GetRestaurantSectionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetRestaurantSectionsRequest.to_json())

# convert the object into a dict
get_restaurant_sections_request_dict = get_restaurant_sections_request_instance.to_dict()
# create an instance of GetRestaurantSectionsRequest from a dict
get_restaurant_sections_request_from_dict = GetRestaurantSectionsRequest.from_dict(get_restaurant_sections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


