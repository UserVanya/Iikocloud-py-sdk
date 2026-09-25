# PreparedChartItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the ingredient written off from stock | [optional] 
**id** | **UUID** | UUID of the ingredient line | [optional] 
**product_id** | **UUID** | UUID of the ingredient product | [optional] 
**product_size_id** | **UUID** | UUID of the product size this line applies to. null — applies to all sizes | [optional] 
**sort_weight** | **float** | Display order weight | [optional] 
**store_specification** | [**StoreSpecification**](StoreSpecification.md) | Department applicability filter for the ingredient line | [optional] 

## Example

```python
from iikocloud_client.models.prepared_chart_item_dto import PreparedChartItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreparedChartItemDto from a JSON string
prepared_chart_item_dto_instance = PreparedChartItemDto.from_json(json)
# print the JSON string representation of the object
print(PreparedChartItemDto.to_json())

# convert the object into a dict
prepared_chart_item_dto_dict = prepared_chart_item_dto_instance.to_dict()
# create an instance of PreparedChartItemDto from a dict
prepared_chart_item_dto_from_dict = PreparedChartItemDto.from_dict(prepared_chart_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


