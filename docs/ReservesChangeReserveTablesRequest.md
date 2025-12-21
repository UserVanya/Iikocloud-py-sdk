# ReservesChangeReserveTablesRequest

Request to change reserve/banquet tables.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve ID. | 
**table_ids** | **List[UUID]** | Table IDs. | 

## Example

```python
from iikocloud_client.models.reserves_change_reserve_tables_request import ReservesChangeReserveTablesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesChangeReserveTablesRequest from a JSON string
reserves_change_reserve_tables_request_instance = ReservesChangeReserveTablesRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesChangeReserveTablesRequest.to_json())

# convert the object into a dict
reserves_change_reserve_tables_request_dict = reserves_change_reserve_tables_request_instance.to_dict()
# create an instance of ReservesChangeReserveTablesRequest from a dict
reserves_change_reserve_tables_request_from_dict = ReservesChangeReserveTablesRequest.from_dict(reserves_change_reserve_tables_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


