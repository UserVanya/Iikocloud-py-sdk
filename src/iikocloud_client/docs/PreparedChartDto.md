# PreparedChartDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembled_quantity** | **float** | Assembled quantity (bookmark rate). Must be greater than 0 | [optional] 
**date_from** | **str** | Start date of the validity period (YYYY-MM-DD or ISO 8601 datetime) | [optional] 
**date_to** | **str** | End date of the validity period; null for an open-ended chart | [optional] 
**direct_writeoff_store_specification** | [**StoreSpecification**](StoreSpecification.md) | Organization (structural unit) filter for DIRECT write-off strategy. null — applies to all organizations | [optional] 
**id** | **UUID** | UUID of the assembly chart | [optional] 
**items** | [**List[PreparedChartItemDto]**](PreparedChartItemDto.md) | Ingredient lines of the assembly chart | [optional] 
**product_id** | **UUID** | UUID of the product this assembly chart belongs to | [optional] 
**product_size_assembly_strategy** | **str** | Size strategy: COMMON (one chart for all sizes) or SPECIFIC (per-size ingredients) | [optional] 

## Example

```python
from iikocloud_client.models.prepared_chart_dto import PreparedChartDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreparedChartDto from a JSON string
prepared_chart_dto_instance = PreparedChartDto.from_json(json)
# print the JSON string representation of the object
print(PreparedChartDto.to_json())

# convert the object into a dict
prepared_chart_dto_dict = prepared_chart_dto_instance.to_dict()
# create an instance of PreparedChartDto from a dict
prepared_chart_dto_from_dict = PreparedChartDto.from_dict(prepared_chart_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


