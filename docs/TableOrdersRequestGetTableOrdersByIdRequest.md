# TableOrdersRequestGetTableOrdersByIdRequest

Request for information about orders using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_keys** | **List[str]** | Source keys. | [optional] 
**organization_ids** | **List[UUID]** | Organization IDs.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_ids** | **List[UUID]** | Order IDs.                &gt; Required if \&quot;posOrderIds\&quot; is null. Must be null if \&quot;posOrderIds\&quot; is not null. | [optional] 
**pos_order_ids** | **List[UUID]** | POS order IDs.                &gt; Required if \&quot;orderIds\&quot; is null. Must be null if \&quot;orderIds\&quot; is not null. | [optional] 
**return_external_data_keys** | **List[str]** | Keys for retrun external data information. | [optional] 

## Example

```python
from iikocloud_client.models.table_orders_request_get_table_orders_by_id_request import TableOrdersRequestGetTableOrdersByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestGetTableOrdersByIdRequest from a JSON string
table_orders_request_get_table_orders_by_id_request_instance = TableOrdersRequestGetTableOrdersByIdRequest.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestGetTableOrdersByIdRequest.to_json())

# convert the object into a dict
table_orders_request_get_table_orders_by_id_request_dict = table_orders_request_get_table_orders_by_id_request_instance.to_dict()
# create an instance of TableOrdersRequestGetTableOrdersByIdRequest from a dict
table_orders_request_get_table_orders_by_id_request_from_dict = TableOrdersRequestGetTableOrdersByIdRequest.from_dict(table_orders_request_get_table_orders_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


