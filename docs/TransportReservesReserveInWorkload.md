# TransportReservesReserveInWorkload

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Banquet/reserve ID. | 
**table_ids** | **List[str]** | Reserved tables. | 
**estimated_start_time** | **str** | Estimated time when reserve will be closed or banquet will be started (Local for the terminal). | 
**duration_in_minutes** | **int** | Estimated banquet duration. | 
**guests_count** | **int** | Number of guests. | 

## Example

```python
from iiko_cloud_client.models.transport_reserves_reserve_in_workload import TransportReservesReserveInWorkload

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesReserveInWorkload from a JSON string
transport_reserves_reserve_in_workload_instance = TransportReservesReserveInWorkload.from_json(json)
# print the JSON string representation of the object
print(TransportReservesReserveInWorkload.to_json())

# convert the object into a dict
transport_reserves_reserve_in_workload_dict = transport_reserves_reserve_in_workload_instance.to_dict()
# create an instance of TransportReservesReserveInWorkload from a dict
transport_reserves_reserve_in_workload_from_dict = TransportReservesReserveInWorkload.from_dict(transport_reserves_reserve_in_workload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


