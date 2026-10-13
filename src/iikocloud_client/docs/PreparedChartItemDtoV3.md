# PreparedChartItemDtoV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the ingredient written off from stock | [optional] 
**id** | **UUID** | UUID of the ingredient line | [optional] 
**product_id** | **UUID** | UUID of the ingredient product written off from stock | [optional] 
**product_size_specification** | **UUID** | UUID of the product size this line applies to. null — applies to all sizes | [optional] 
**sort_weight** | **float** | Display order weight | [optional] 
**store_specification** | [**StoreSpecificationV3**](StoreSpecificationV3.md) | Departments (organizations) where the ingredient line applies | [optional] 

## Example

```python
from iikocloud_client.models.prepared_chart_item_dto_v3 import PreparedChartItemDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of PreparedChartItemDtoV3 from a JSON string
prepared_chart_item_dto_v3_instance = PreparedChartItemDtoV3.from_json(json)
# print the JSON string representation of the object
print(PreparedChartItemDtoV3.to_json())

# convert the object into a dict
prepared_chart_item_dto_v3_dict = prepared_chart_item_dto_v3_instance.to_dict()
# create an instance of PreparedChartItemDtoV3 from a dict
prepared_chart_item_dto_v3_from_dict = PreparedChartItemDtoV3.from_dict(prepared_chart_item_dto_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


