# CostPriceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_factor** | **float** | Quantity factor | [optional] 
**is_evaluative** | **bool** | Estimated price flag | [optional] 
**product_id** | **str** | Product identifier (GUID) | [optional] 
**product_size** | **str** | Product size identifier (GUID) | [optional] 
**store_id** | **str** | Store identifier (GUID) | [optional] 
**value** | **float** | Cost price value | [optional] 

## Example

```python
from iikocloud_client.models.cost_price_item import CostPriceItem

# TODO update the JSON string below
json = "{}"
# create an instance of CostPriceItem from a JSON string
cost_price_item_instance = CostPriceItem.from_json(json)
# print the JSON string representation of the object
print(CostPriceItem.to_json())

# convert the object into a dict
cost_price_item_dict = cost_price_item_instance.to_dict()
# create an instance of CostPriceItem from a dict
cost_price_item_from_dict = CostPriceItem.from_dict(cost_price_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


