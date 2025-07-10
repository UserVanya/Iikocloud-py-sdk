# TransportReservesReservesResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**reserves** | [**List[TransportReservesReserveInfo]**](TransportReservesReserveInfo.md) | Banquets/reserves. | 

## Example

```python
from iiko_cloud_client.models.transport_reserves_reserves_response import TransportReservesReservesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesReservesResponse from a JSON string
transport_reserves_reserves_response_instance = TransportReservesReservesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportReservesReservesResponse.to_json())

# convert the object into a dict
transport_reserves_reserves_response_dict = transport_reserves_reserves_response_instance.to_dict()
# create an instance of TransportReservesReservesResponse from a dict
transport_reserves_reserves_response_from_dict = TransportReservesReservesResponse.from_dict(transport_reserves_reserves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


