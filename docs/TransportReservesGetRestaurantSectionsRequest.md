# TransportReservesGetRestaurantSectionsRequest

Request for get all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_ids** | **List[str]** | Collection of terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**return_schema** | **bool** | Indicates whether table layout information should be returned... | [optional] 
**revision** | **int** | Last modified time after. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_reserves_get_restaurant_sections_request import TransportReservesGetRestaurantSectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesGetRestaurantSectionsRequest from a JSON string
transport_reserves_get_restaurant_sections_request_instance = TransportReservesGetRestaurantSectionsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportReservesGetRestaurantSectionsRequest.to_json())

# convert the object into a dict
transport_reserves_get_restaurant_sections_request_dict = transport_reserves_get_restaurant_sections_request_instance.to_dict()
# create an instance of TransportReservesGetRestaurantSectionsRequest from a dict
transport_reserves_get_restaurant_sections_request_from_dict = TransportReservesGetRestaurantSectionsRequest.from_dict(transport_reserves_get_restaurant_sections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


