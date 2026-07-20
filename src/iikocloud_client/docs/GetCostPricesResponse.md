# GetCostPricesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CostPriceItem]**](CostPriceItem.md) | List of item cost prices | [optional] 
**problem_items** | [**List[PriceItem]**](PriceItem.md) | List of problem items | [optional] 

## Example

```python
from iikocloud_client.models.get_cost_prices_response import GetCostPricesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCostPricesResponse from a JSON string
get_cost_prices_response_instance = GetCostPricesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCostPricesResponse.to_json())

# convert the object into a dict
get_cost_prices_response_dict = get_cost_prices_response_instance.to_dict()
# create an instance of GetCostPricesResponse from a dict
get_cost_prices_response_from_dict = GetCostPricesResponse.from_dict(get_cost_prices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


