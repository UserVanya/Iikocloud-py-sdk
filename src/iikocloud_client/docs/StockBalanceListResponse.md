# StockBalanceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_at** | **str** | Balance calculation moment echoed from the request without changes | [optional] 
**currency_code** | **str** | Organization currency code (ISO 4217 alpha-3) | [optional] 
**generated_at** | **str** | Response generation time in RFC 3339 UTC format | [optional] 
**items** | [**List[StockBalanceItem]**](StockBalanceItem.md) | Rows of non-zero balances | [optional] 
**limit** | **int** | Limit value from the request | [optional] 
**offset** | **int** | Offset value from the request | [optional] 
**organization_id** | **UUID** | Organization identifier (GUID) echoed from the request | [optional] 
**total_count** | **int** | Total number of rows before pagination | [optional] 

## Example

```python
from iikocloud_client.models.stock_balance_list_response import StockBalanceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StockBalanceListResponse from a JSON string
stock_balance_list_response_instance = StockBalanceListResponse.from_json(json)
# print the JSON string representation of the object
print(StockBalanceListResponse.to_json())

# convert the object into a dict
stock_balance_list_response_dict = stock_balance_list_response_instance.to_dict()
# create an instance of StockBalanceListResponse from a dict
stock_balance_list_response_from_dict = StockBalanceListResponse.from_dict(stock_balance_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


