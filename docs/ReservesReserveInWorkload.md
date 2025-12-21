# ReservesReserveInWorkload

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Banquet/reserve ID. | 
**table_ids** | **List[UUID]** | Reserved tables. | 
**estimated_start_time** | **str** | Estimated time when reserve will be closed or banquet will be started (Local for the terminal). | 
**duration_in_minutes** | **int** | Estimated banquet duration. | 
**guests_count** | **int** | Number of guests. | 

## Example

```python
from iikocloud_client.models.reserves_reserve_in_workload import ReservesReserveInWorkload

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesReserveInWorkload from a JSON string
reserves_reserve_in_workload_instance = ReservesReserveInWorkload.from_json(json)
# print the JSON string representation of the object
print(ReservesReserveInWorkload.to_json())

# convert the object into a dict
reserves_reserve_in_workload_dict = reserves_reserve_in_workload_instance.to_dict()
# create an instance of ReservesReserveInWorkload from a dict
reserves_reserve_in_workload_from_dict = ReservesReserveInWorkload.from_dict(reserves_reserve_in_workload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


