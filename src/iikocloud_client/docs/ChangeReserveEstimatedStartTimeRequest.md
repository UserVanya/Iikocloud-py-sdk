# ChangeReserveEstimatedStartTimeRequest

Request to change reserve/banquet estimated start time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_estimated_start_time** | **str** | New estimated start time of reserve/banquet. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve/banquet ID. | 

## Example

```python
from iikocloud_client.models.change_reserve_estimated_start_time_request import ChangeReserveEstimatedStartTimeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeReserveEstimatedStartTimeRequest from a JSON string
change_reserve_estimated_start_time_request_instance = ChangeReserveEstimatedStartTimeRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeReserveEstimatedStartTimeRequest.to_json())

# convert the object into a dict
change_reserve_estimated_start_time_request_dict = change_reserve_estimated_start_time_request_instance.to_dict()
# create an instance of ChangeReserveEstimatedStartTimeRequest from a dict
change_reserve_estimated_start_time_request_from_dict = ChangeReserveEstimatedStartTimeRequest.from_dict(change_reserve_estimated_start_time_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


