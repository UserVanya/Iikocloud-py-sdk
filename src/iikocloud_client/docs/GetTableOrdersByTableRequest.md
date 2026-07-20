# GetTableOrdersByTableRequest

Request for information about orders using table IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Order creation date (terminal time zone). Lower limit.                Order details are stored for 90 days. | [optional] 
**date_to** | **str** | Order creation date (terminal time zone). Upper limit. | [optional] 
**organization_ids** | **List[UUID]** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**source_keys** | **List[str]** | Source keys. | [optional] 
**statuses** | [**List[OrderStatus]**](OrderStatus.md) | Order statuses. | [optional] 
**table_ids** | **List[UUID]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_table_orders_by_table_request import GetTableOrdersByTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTableOrdersByTableRequest from a JSON string
get_table_orders_by_table_request_instance = GetTableOrdersByTableRequest.from_json(json)
# print the JSON string representation of the object
print(GetTableOrdersByTableRequest.to_json())

# convert the object into a dict
get_table_orders_by_table_request_dict = get_table_orders_by_table_request_instance.to_dict()
# create an instance of GetTableOrdersByTableRequest from a dict
get_table_orders_by_table_request_from_dict = GetTableOrdersByTableRequest.from_dict(get_table_orders_by_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


