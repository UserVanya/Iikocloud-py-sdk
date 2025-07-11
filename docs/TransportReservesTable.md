# TransportReservesTable

Table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Table ID. | 
**number** | **int** | Number of table. | 
**name** | **str** | Table name specified in the organization settings. | 
**seating_capacity** | **int** | Seating capacity of the table. | 
**revision** | **int** | Last modified time. | 
**is_deleted** | **bool** | Is table deleted. | 
**pos_id** | **str** | POS table Id. | 

## Example

```python
from iikocloud_client.models.transport_reserves_table import TransportReservesTable

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesTable from a JSON string
transport_reserves_table_instance = TransportReservesTable.from_json(json)
# print the JSON string representation of the object
print(TransportReservesTable.to_json())

# convert the object into a dict
transport_reserves_table_dict = transport_reserves_table_instance.to_dict()
# create an instance of TransportReservesTable from a dict
transport_reserves_table_from_dict = TransportReservesTable.from_dict(transport_reserves_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


