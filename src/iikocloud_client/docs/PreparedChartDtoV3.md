# PreparedChartDtoV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembled_amount** | **float** | Bookmark rate of the prepared dish | [optional] 
**date_from** | **str** | Start date of the validity period (YYYY-MM-DD) | [optional] 
**date_to** | **str** | End date of the validity period (YYYY-MM-DD) | [optional] 
**id** | **UUID** | UUID of the assembly chart | [optional] 
**items** | [**List[PreparedChartItemDtoV3]**](PreparedChartItemDtoV3.md) | Ingredient lines of the assembly chart | [optional] 
**product_id** | **UUID** | UUID of the product this breakdown belongs to | [optional] 
**product_size_assembly_strategy** | **str** | Size strategy: COMMON (one chart for all sizes) or SPECIFIC (per-size ingredients) | [optional] 

## Example

```python
from iikocloud_client.models.prepared_chart_dto_v3 import PreparedChartDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of PreparedChartDtoV3 from a JSON string
prepared_chart_dto_v3_instance = PreparedChartDtoV3.from_json(json)
# print the JSON string representation of the object
print(PreparedChartDtoV3.to_json())

# convert the object into a dict
prepared_chart_dto_v3_dict = prepared_chart_dto_v3_instance.to_dict()
# create an instance of PreparedChartDtoV3 from a dict
prepared_chart_dto_v3_from_dict = PreparedChartDtoV3.from_dict(prepared_chart_dto_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


