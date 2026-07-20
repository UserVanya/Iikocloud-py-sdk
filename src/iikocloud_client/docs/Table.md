# Table

Table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Table ID. | 
**is_deleted** | **bool** | Is table deleted. | 
**name** | **str** | Table name specified in the organization settings. | 
**number** | **int** | Number of table. | 
**pos_id** | **UUID** | POS table Id. | 
**revision** | **int** | Last modified time. | 
**seating_capacity** | **int** | Seating capacity of the table. | 

## Example

```python
from iikocloud_client.models.table import Table

# TODO update the JSON string below
json = "{}"
# create an instance of Table from a JSON string
table_instance = Table.from_json(json)
# print the JSON string representation of the object
print(Table.to_json())

# convert the object into a dict
table_dict = table_instance.to_dict()
# create an instance of Table from a dict
table_from_dict = Table.from_dict(table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


