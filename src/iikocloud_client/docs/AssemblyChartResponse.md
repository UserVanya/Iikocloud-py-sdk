# AssemblyChartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appearance** | **str** | Presentation and serving requirements (up to 2000 characters) | [optional] 
**assembled_quantity** | **float** | Assembled quantity (bookmark rate). Must be greater than 0 | [optional] 
**date_from** | **str** | Start date of the validity period (YYYY-MM-DD or ISO 8601 datetime) | [optional] 
**date_to** | **str** | End date of the validity period; null for an open-ended chart | [optional] 
**description** | **str** | Free-text description field (up to 2000 characters) | [optional] 
**direct_writeoff_store_specification** | [**StoreSpecification**](StoreSpecification.md) | Organization (structural unit) filter for DIRECT write-off strategy. null — applies to all organizations | [optional] 
**id** | **UUID** | UUID of the assembly chart | [optional] 
**items** | [**List[AssemblyChartItemResponse]**](AssemblyChartItemResponse.md) | Ingredient lines of the assembly chart | [optional] 
**organoleptic** | **str** | Organoleptic quality indicators (up to 2000 characters) | [optional] 
**output_comment** | **str** | Output comment / yield note (up to 2000 characters) | [optional] 
**product_id** | **UUID** | UUID of the product this assembly chart belongs to | [optional] 
**product_size_assembly_strategy** | **str** | Size strategy: COMMON (one chart for all sizes) or SPECIFIC (per-size ingredients) | [optional] 
**technology_description** | **str** | Preparation technology description (up to 2000 characters) | [optional] 
**writeoff_strategy** | **str** | Write-off strategy: ASSEMBLE (write off ingredients) or DIRECT (write off the product itself) | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_response import AssemblyChartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartResponse from a JSON string
assembly_chart_response_instance = AssemblyChartResponse.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartResponse.to_json())

# convert the object into a dict
assembly_chart_response_dict = assembly_chart_response_instance.to_dict()
# create an instance of AssemblyChartResponse from a dict
assembly_chart_response_from_dict = AssemblyChartResponse.from_dict(assembly_chart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


