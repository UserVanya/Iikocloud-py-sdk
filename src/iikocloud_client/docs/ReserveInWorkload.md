# ReserveInWorkload

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_in_minutes** | **int** | Estimated banquet duration. | 
**estimated_start_time** | **str** | Estimated time when reserve will be closed or banquet will be started (Local for the terminal). | 
**guests_count** | **int** | Number of guests. | 
**id** | **UUID** | Banquet/reserve ID. | 
**table_ids** | **List[UUID]** | Reserved tables. | 

## Example

```python
from iikocloud_client.models.reserve_in_workload import ReserveInWorkload

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveInWorkload from a JSON string
reserve_in_workload_instance = ReserveInWorkload.from_json(json)
# print the JSON string representation of the object
print(ReserveInWorkload.to_json())

# convert the object into a dict
reserve_in_workload_dict = reserve_in_workload_instance.to_dict()
# create an instance of ReserveInWorkload from a dict
reserve_in_workload_from_dict = ReserveInWorkload.from_dict(reserve_in_workload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


