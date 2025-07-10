# TransportTableOrdersRequestGuestsInfo

Table order guests information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Guests count. | 

## Example

```python
from iiko_cloud_client.models.transport_table_orders_request_guests_info import TransportTableOrdersRequestGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestGuestsInfo from a JSON string
transport_table_orders_request_guests_info_instance = TransportTableOrdersRequestGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestGuestsInfo.to_json())

# convert the object into a dict
transport_table_orders_request_guests_info_dict = transport_table_orders_request_guests_info_instance.to_dict()
# create an instance of TransportTableOrdersRequestGuestsInfo from a dict
transport_table_orders_request_guests_info_from_dict = TransportTableOrdersRequestGuestsInfo.from_dict(transport_table_orders_request_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


