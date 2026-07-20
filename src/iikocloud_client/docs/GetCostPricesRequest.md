# GetCostPricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_incoming** | **str** | Date for cost price calculation (ISO8601 format, e.g. 2025-12-26T12:40:26.801+03:00) | 
**items** | [**List[PriceItem]**](PriceItem.md) | List of nomenclature items for cost price retrieval | 
**organization_id** | **str** | Organization identifier (GUID) | 

## Example

```python
from iikocloud_client.models.get_cost_prices_request import GetCostPricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCostPricesRequest from a JSON string
get_cost_prices_request_instance = GetCostPricesRequest.from_json(json)
# print the JSON string representation of the object
print(GetCostPricesRequest.to_json())

# convert the object into a dict
get_cost_prices_request_dict = get_cost_prices_request_instance.to_dict()
# create an instance of GetCostPricesRequest from a dict
get_cost_prices_request_from_dict = GetCostPricesRequest.from_dict(get_cost_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


