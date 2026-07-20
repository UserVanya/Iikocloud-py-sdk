# ReservesResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**reserves** | [**List[ReserveInfo]**](ReserveInfo.md) | Banquets/reserves. | 

## Example

```python
from iikocloud_client.models.reserves_response import ReservesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesResponse from a JSON string
reserves_response_instance = ReservesResponse.from_json(json)
# print the JSON string representation of the object
print(ReservesResponse.to_json())

# convert the object into a dict
reserves_response_dict = reserves_response_instance.to_dict()
# create an instance of ReservesResponse from a dict
reserves_response_from_dict = ReservesResponse.from_dict(reserves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


