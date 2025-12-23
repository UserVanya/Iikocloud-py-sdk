# TableOrdersRequestGetTableOrdersByTableRequest

Request for information about orders using table IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_keys** | **List[str]** | Source keys. | [optional] 
**organization_ids** | **List[str]** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**table_ids** | **List[str]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | 
**statuses** | [**List[OrdersCommonOrderStatus]**](OrdersCommonOrderStatus.md) | Order statuses. | [optional] 
**date_from** | **str** | Order creation date (terminal time zone). Lower limit.                Order details are stored for 90 days. | [optional] 
**date_to** | **str** | Order creation date (terminal time zone). Upper limit. | [optional] 

## Example

```python
from iikocloud_client.models.table_orders_request_get_table_orders_by_table_request import TableOrdersRequestGetTableOrdersByTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestGetTableOrdersByTableRequest from a JSON string
table_orders_request_get_table_orders_by_table_request_instance = TableOrdersRequestGetTableOrdersByTableRequest.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestGetTableOrdersByTableRequest.to_json())

# convert the object into a dict
table_orders_request_get_table_orders_by_table_request_dict = table_orders_request_get_table_orders_by_table_request_instance.to_dict()
# create an instance of TableOrdersRequestGetTableOrdersByTableRequest from a dict
table_orders_request_get_table_orders_by_table_request_from_dict = TableOrdersRequestGetTableOrdersByTableRequest.from_dict(table_orders_request_get_table_orders_by_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


