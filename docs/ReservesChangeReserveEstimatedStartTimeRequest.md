# ReservesChangeReserveEstimatedStartTimeRequest

Request to change reserve/banquet estimated start time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve/banquet ID. | 
**new_estimated_start_time** | **str** | New estimated start time of reserve/banquet. | 

## Example

```python
from iikocloud_client.models.reserves_change_reserve_estimated_start_time_request import ReservesChangeReserveEstimatedStartTimeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesChangeReserveEstimatedStartTimeRequest from a JSON string
reserves_change_reserve_estimated_start_time_request_instance = ReservesChangeReserveEstimatedStartTimeRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesChangeReserveEstimatedStartTimeRequest.to_json())

# convert the object into a dict
reserves_change_reserve_estimated_start_time_request_dict = reserves_change_reserve_estimated_start_time_request_instance.to_dict()
# create an instance of ReservesChangeReserveEstimatedStartTimeRequest from a dict
reserves_change_reserve_estimated_start_time_request_from_dict = ReservesChangeReserveEstimatedStartTimeRequest.from_dict(reserves_change_reserve_estimated_start_time_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


