# ChangeReserveTablesRequest

Request to change reserve/banquet tables.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve ID. | 
**table_ids** | **List[UUID]** | Table IDs. | 

## Example

```python
from iikocloud_client.models.change_reserve_tables_request import ChangeReserveTablesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeReserveTablesRequest from a JSON string
change_reserve_tables_request_instance = ChangeReserveTablesRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeReserveTablesRequest.to_json())

# convert the object into a dict
change_reserve_tables_request_dict = change_reserve_tables_request_instance.to_dict()
# create an instance of ChangeReserveTablesRequest from a dict
change_reserve_tables_request_from_dict = ChangeReserveTablesRequest.from_dict(change_reserve_tables_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


