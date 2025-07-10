# TransportReservesReserveResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**reserve_info** | [**TransportReservesReserveInfo**](TransportReservesReserveInfo.md) | Banquet/reserve. | 

## Example

```python
from iiko_cloud_client.models.transport_reserves_reserve_response import TransportReservesReserveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesReserveResponse from a JSON string
transport_reserves_reserve_response_instance = TransportReservesReserveResponse.from_json(json)
# print the JSON string representation of the object
print(TransportReservesReserveResponse.to_json())

# convert the object into a dict
transport_reserves_reserve_response_dict = transport_reserves_reserve_response_instance.to_dict()
# create an instance of TransportReservesReserveResponse from a dict
transport_reserves_reserve_response_from_dict = TransportReservesReserveResponse.from_dict(transport_reserves_reserve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


