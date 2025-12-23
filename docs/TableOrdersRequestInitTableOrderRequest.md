# TableOrdersRequestInitTableOrderRequest

Request for init orders on table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**table_ids** | **List[str]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | 

## Example

```python
from iikocloud_client.models.table_orders_request_init_table_order_request import TableOrdersRequestInitTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestInitTableOrderRequest from a JSON string
table_orders_request_init_table_order_request_instance = TableOrdersRequestInitTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestInitTableOrderRequest.to_json())

# convert the object into a dict
table_orders_request_init_table_order_request_dict = table_orders_request_init_table_order_request_instance.to_dict()
# create an instance of TableOrdersRequestInitTableOrderRequest from a dict
table_orders_request_init_table_order_request_from_dict = TableOrdersRequestInitTableOrderRequest.from_dict(table_orders_request_init_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


