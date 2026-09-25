# StockBalanceListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_at** | **str** | Balance calculation moment in RFC 3339 format; timezone offset is optional (UTC when absent); returned unchanged in the response | 
**limit** | **int** | Maximum number of rows in the page, from 1 to 1000; default 50 | [optional] 
**offset** | **int** | Number of rows to skip; non-negative; default 0 | [optional] 
**organization_id** | **UUID** | Organization identifier (GUID) | [optional] 
**product_group_ids** | **List[UUID]** | Product group identifiers (GUID); products of these groups are included recursively with subgroups. Non-empty unique array of up to 1000 items | [optional] 
**product_ids** | **List[UUID]** | Product identifiers (GUID); if absent — all products with non-zero balances. Non-empty unique array of up to 1000 items | [optional] 
**should_include_details** | **bool** | Flag to include current reference details for the response rows; default false | [optional] 
**store_ids** | **List[UUID]** | Store identifiers (GUID); if absent — all organization stores. Non-empty unique array of up to 1000 items | [optional] 

## Example

```python
from iikocloud_client.models.stock_balance_list_request import StockBalanceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockBalanceListRequest from a JSON string
stock_balance_list_request_instance = StockBalanceListRequest.from_json(json)
# print the JSON string representation of the object
print(StockBalanceListRequest.to_json())

# convert the object into a dict
stock_balance_list_request_dict = stock_balance_list_request_instance.to_dict()
# create an instance of StockBalanceListRequest from a dict
stock_balance_list_request_from_dict = StockBalanceListRequest.from_dict(stock_balance_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


