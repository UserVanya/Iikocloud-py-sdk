# ReservesTable

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
from iikocloud_client.models.reserves_table import ReservesTable

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesTable from a JSON string
reserves_table_instance = ReservesTable.from_json(json)
# print the JSON string representation of the object
print(ReservesTable.to_json())

# convert the object into a dict
reserves_table_dict = reserves_table_instance.to_dict()
# create an instance of ReservesTable from a dict
reserves_table_from_dict = ReservesTable.from_dict(reserves_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


