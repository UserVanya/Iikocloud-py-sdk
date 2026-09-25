# AssemblyChartV1SaveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appearance** | **str** | Presentation and serving requirements (up to 2000 characters) | [optional] 
**assembled_amount** | **float** | Assembled amount (bookmark rate). Must be greater than 0 | [optional] 
**date_from** | **str** | Start date of the validity period (YYYY-MM-DD or ISO 8601 datetime) | [optional] 
**date_to** | **str** | End date of the validity period; null for an open-ended chart | [optional] 
**description** | **str** | Free-text description field (up to 2000 characters) | [optional] 
**direct_writeoff_store_specification** | [**StoreSpecification**](StoreSpecification.md) | Department filter for DIRECT write-off strategy. null — applies to all departments | [optional] 
**franchise_master_id** | **str** | Franchise master UUID. null — not a franchise object | [optional] 
**franchise_original_id** | **str** | Franchise original UUID. null — not a franchise object | [optional] 
**franchise_unique_id** | **str** | Franchise unique UUID. Required when franchiseMasterId is set | [optional] 
**id** | **str** | UUID of the assembly chart | [optional] 
**items** | [**List[AssemblyChartItem]**](AssemblyChartItem.md) | Ingredient lines of the assembly chart | [optional] 
**organoleptic** | **str** | Organoleptic quality indicators (up to 2000 characters) | [optional] 
**output_comment** | **str** | Output comment / yield note (up to 2000 characters) | [optional] 
**picture** | **str** | UUID of the technology image. null — no image | [optional] 
**product** | **str** | UUID of the product this assembly chart belongs to | [optional] 
**product_size_assembly_strategy** | **str** | Size strategy: COMMON (one chart for all sizes) or SPECIFIC (per-size ingredients) | [optional] 
**technology_description** | **str** | Preparation technology description (up to 2000 characters) | [optional] 
**version_compatibility** | **str** | Version compatibility tag. Only V_7_0 is currently accepted | [optional] 
**writeoff_strategy** | **str** | Write-off strategy: ASSEMBLE (write off ingredients) or DIRECT (write off the product itself) | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_v1_save_request import AssemblyChartV1SaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartV1SaveRequest from a JSON string
assembly_chart_v1_save_request_instance = AssemblyChartV1SaveRequest.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartV1SaveRequest.to_json())

# convert the object into a dict
assembly_chart_v1_save_request_dict = assembly_chart_v1_save_request_instance.to_dict()
# create an instance of AssemblyChartV1SaveRequest from a dict
assembly_chart_v1_save_request_from_dict = AssemblyChartV1SaveRequest.from_dict(assembly_chart_v1_save_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


