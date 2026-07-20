# GetTableOrdersByIdRequest

Request for information about orders using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[UUID]** | Order IDs.                &gt; Required if \&quot;posOrderIds\&quot; is null. Must be null if \&quot;posOrderIds\&quot; is not null. | [optional] 
**organization_ids** | **List[UUID]** | Organization IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**pos_order_ids** | **List[UUID]** | POS order IDs.                &gt; Required if \&quot;orderIds\&quot; is null. Must be null if \&quot;orderIds\&quot; is not null. | [optional] 
**return_external_data_keys** | **List[str]** | Keys for retrun external data information. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 

## Example

```python
from iikocloud_client.models.get_table_orders_by_id_request import GetTableOrdersByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTableOrdersByIdRequest from a JSON string
get_table_orders_by_id_request_instance = GetTableOrdersByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetTableOrdersByIdRequest.to_json())

# convert the object into a dict
get_table_orders_by_id_request_dict = get_table_orders_by_id_request_instance.to_dict()
# create an instance of GetTableOrdersByIdRequest from a dict
get_table_orders_by_id_request_from_dict = GetTableOrdersByIdRequest.from_dict(get_table_orders_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


