# ReservesReserveResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**reserve_info** | [**ReservesReserveInfo**](ReservesReserveInfo.md) | Banquet/reserve. | 

## Example

```python
from iikocloud_client.models.reserves_reserve_response import ReservesReserveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesReserveResponse from a JSON string
reserves_reserve_response_instance = ReservesReserveResponse.from_json(json)
# print the JSON string representation of the object
print(ReservesReserveResponse.to_json())

# convert the object into a dict
reserves_reserve_response_dict = reserves_reserve_response_instance.to_dict()
# create an instance of ReservesReserveResponse from a dict
reserves_reserve_response_from_dict = ReservesReserveResponse.from_dict(reserves_reserve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


