# TableOrdersRequestGuestsInfo

Table order guests information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Guests count. | 

## Example

```python
from iikocloud_client.models.table_orders_request_guests_info import TableOrdersRequestGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestGuestsInfo from a JSON string
table_orders_request_guests_info_instance = TableOrdersRequestGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestGuestsInfo.to_json())

# convert the object into a dict
table_orders_request_guests_info_dict = table_orders_request_guests_info_instance.to_dict()
# create an instance of TableOrdersRequestGuestsInfo from a dict
table_orders_request_guests_info_from_dict = TableOrdersRequestGuestsInfo.from_dict(table_orders_request_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


