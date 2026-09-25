# StockBalanceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_sum** | **float** | Cost sum in the organization currency | [optional] 
**details** | [**StockBalanceDetails**](StockBalanceDetails.md) | Current reference details of the row; null when shouldIncludeDetails is false | [optional] 
**organization_id** | **UUID** | Organization identifier (GUID) | [optional] 
**product_id** | **UUID** | Product identifier (GUID) | [optional] 
**quantity** | **float** | Quantity in the main unit of the product | [optional] 
**store_id** | **UUID** | Store identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.stock_balance_item import StockBalanceItem

# TODO update the JSON string below
json = "{}"
# create an instance of StockBalanceItem from a JSON string
stock_balance_item_instance = StockBalanceItem.from_json(json)
# print the JSON string representation of the object
print(StockBalanceItem.to_json())

# convert the object into a dict
stock_balance_item_dict = stock_balance_item_instance.to_dict()
# create an instance of StockBalanceItem from a dict
stock_balance_item_from_dict = StockBalanceItem.from_dict(stock_balance_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


