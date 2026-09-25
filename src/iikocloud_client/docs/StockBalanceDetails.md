# StockBalanceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_unit_id** | **UUID** | Main product unit identifier (GUID) | [optional] 
**amount_unit_name** | **str** | Main product unit name | [optional] 
**maximum_quantity** | **float** | Effective maximum quantity level for the store (v1: always 0) | [optional] 
**minimum_quantity** | **float** | Effective minimum quantity level for the store (v1: always 0) | [optional] 
**parent_group_id** | **UUID** | Immediate parent group identifier (GUID); null if no group is set | [optional] 
**parent_group_name** | **str** | Immediate parent group name; null if no group is set | [optional] 
**product_name** | **str** | Current product name | [optional] 
**store_display_name** | **str** | Display name in the form storeParentName: storeName | [optional] 
**store_name** | **str** | Current store name | [optional] 
**store_parent_id** | **UUID** | Structural parent of the store (organization identifier in v1) | [optional] 
**store_parent_name** | **str** | Name of the structural parent of the store (organization name in v1) | [optional] 

## Example

```python
from iikocloud_client.models.stock_balance_details import StockBalanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StockBalanceDetails from a JSON string
stock_balance_details_instance = StockBalanceDetails.from_json(json)
# print the JSON string representation of the object
print(StockBalanceDetails.to_json())

# convert the object into a dict
stock_balance_details_dict = stock_balance_details_instance.to_dict()
# create an instance of StockBalanceDetails from a dict
stock_balance_details_from_dict = StockBalanceDetails.from_dict(stock_balance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


