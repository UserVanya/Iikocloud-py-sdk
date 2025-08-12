# TransportTableOrdersRequestGetTableOrdersByIdRequest

Request for information about orders using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_keys** | **List[str]** | Source keys. | [optional] 
**organization_ids** | **List[str]** | Organization IDs.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_ids** | **List[str]** | Order IDs.                &gt; Required if \&quot;posOrderIds\&quot; is null. Must be null if \&quot;posOrderIds\&quot; is not null. | [optional] 
**pos_order_ids** | **List[str]** | POS order IDs.                &gt; Required if \&quot;orderIds\&quot; is null. Must be null if \&quot;orderIds\&quot; is not null. | [optional] 
**return_external_data_keys** | **List[str]** | Keys for retrun external data information. | [optional] 

## Example

```python
from iikocloud_client.models.transport_table_orders_request_get_table_orders_by_id_request import TransportTableOrdersRequestGetTableOrdersByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestGetTableOrdersByIdRequest from a JSON string
transport_table_orders_request_get_table_orders_by_id_request_instance = TransportTableOrdersRequestGetTableOrdersByIdRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestGetTableOrdersByIdRequest.to_json())

# convert the object into a dict
transport_table_orders_request_get_table_orders_by_id_request_dict = transport_table_orders_request_get_table_orders_by_id_request_instance.to_dict()
# create an instance of TransportTableOrdersRequestGetTableOrdersByIdRequest from a dict
transport_table_orders_request_get_table_orders_by_id_request_from_dict = TransportTableOrdersRequestGetTableOrdersByIdRequest.from_dict(transport_table_orders_request_get_table_orders_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


