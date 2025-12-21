# ReservesReservesResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**reserves** | [**List[ReservesReserveInfo]**](ReservesReserveInfo.md) | Banquets/reserves. | 

## Example

```python
from iikocloud_client.models.reserves_reserves_response import ReservesReservesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesReservesResponse from a JSON string
reserves_reserves_response_instance = ReservesReservesResponse.from_json(json)
# print the JSON string representation of the object
print(ReservesReservesResponse.to_json())

# convert the object into a dict
reserves_reserves_response_dict = reserves_reserves_response_instance.to_dict()
# create an instance of ReservesReservesResponse from a dict
reserves_reserves_response_from_dict = ReservesReservesResponse.from_dict(reserves_reserves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


