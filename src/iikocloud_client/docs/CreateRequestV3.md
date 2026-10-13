# CreateRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appearance** | **str** | Presentation and serving requirements (up to 2000 characters) | [optional] 
**assembled_quantity** | **float** | Assembled quantity (bookmark rate). Must be greater than 0 | [optional] 
**date_from** | **str** | Start date of the validity period (YYYY-MM-DD) | [optional] 
**date_to** | **str** | End date of the validity period (YYYY-MM-DD) | 
**description** | **str** | Free-text description field (up to 2000 characters) | [optional] 
**direct_writeoff_store_specification** | [**StoreSpecificationV3**](StoreSpecificationV3.md) | Organization (structural unit) filter for DIRECT write-off strategy. null — applies to all organizations | [optional] 
**franchise_master_id** | **UUID** | Franchise master UUID. null — not a franchise object | [optional] 
**franchise_original_id** | **UUID** | Franchise original UUID. null — not a franchise object | [optional] 
**franchise_unique_id** | **UUID** | Franchise unique UUID. Required when franchiseMasterId is set | [optional] 
**id** | **UUID** | UUID of the assembly chart | [optional] 
**items** | [**List[AssemblyChartItemV3]**](AssemblyChartItemV3.md) | Ingredient lines of the assembly chart | [optional] 
**organoleptic** | **str** | Organoleptic quality indicators (up to 2000 characters) | [optional] 
**output_comment** | **str** | Output comment / yield note (up to 2000 characters) | [optional] 
**picture** | **str** | UUID of the technology image. null — no image | [optional] 
**product_id** | **UUID** | UUID of the product this assembly chart belongs to | [optional] 
**product_size_assembly_strategy** | **str** | Size strategy: COMMON (one chart for all sizes) or SPECIFIC (per-size ingredients) | [optional] 
**technology_description** | **str** | Preparation technology description (up to 2000 characters) | [optional] 
**version_compatibility** | **str** | Version compatibility tag. Only V_7_0 is currently accepted | [optional] 
**writeoff_strategy** | **str** | Write-off strategy: ASSEMBLE (write off ingredients) or DIRECT (write off the product itself) | [optional] 

## Example

```python
from iikocloud_client.models.create_request_v3 import CreateRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestV3 from a JSON string
create_request_v3_instance = CreateRequestV3.from_json(json)
# print the JSON string representation of the object
print(CreateRequestV3.to_json())

# convert the object into a dict
create_request_v3_dict = create_request_v3_instance.to_dict()
# create an instance of CreateRequestV3 from a dict
create_request_v3_from_dict = CreateRequestV3.from_dict(create_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


