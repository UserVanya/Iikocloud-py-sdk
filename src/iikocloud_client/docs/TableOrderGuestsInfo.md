# TableOrderGuestsInfo

Table order guests information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Guests count. | 

## Example

```python
from iikocloud_client.models.table_order_guests_info import TableOrderGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderGuestsInfo from a JSON string
table_order_guests_info_instance = TableOrderGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(TableOrderGuestsInfo.to_json())

# convert the object into a dict
table_order_guests_info_dict = table_order_guests_info_instance.to_dict()
# create an instance of TableOrderGuestsInfo from a dict
table_order_guests_info_from_dict = TableOrderGuestsInfo.from_dict(table_order_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


