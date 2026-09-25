# ChartTreeNodeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembled_quantity** | **float** | Assembled quantity (bookmark rate). Must be greater than 0 | [optional] 
**has_chart** | **bool** | true — the product has its own assembly chart for the given date (items contains its composition); false — the product is an elementary store item | [optional] 
**id** | **UUID** | UUID of the assembly chart | [optional] 
**items** | [**List[ChartTreeNodeDto]**](ChartTreeNodeDto.md) | Child nodes of the tree — ingredients of the assembly chart, each recursively expanded with its own composition (if it has an assembly chart) | [optional] 
**package_count** | **float** | Package count | [optional] 
**package_type_id** | **UUID** | UUID of the package type | [optional] 
**product_id** | **UUID** | UUID of the product this assembly chart belongs to | [optional] 
**product_size_assembly_strategy** | **str** | Size strategy: COMMON (one chart for all sizes) or SPECIFIC (per-size ingredients) | [optional] 
**quantity_in** | **float** | Gross quantity (brutto) | [optional] 
**quantity_middle** | **float** | Semi-processed quantity (netto) | [optional] 
**quantity_out** | **float** | Finished quantity (yield) | [optional] 
**writeoff_strategy** | **str** | Write-off strategy: ASSEMBLE (write off ingredients) or DIRECT (write off the product itself) | [optional] 

## Example

```python
from iikocloud_client.models.chart_tree_node_dto import ChartTreeNodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChartTreeNodeDto from a JSON string
chart_tree_node_dto_instance = ChartTreeNodeDto.from_json(json)
# print the JSON string representation of the object
print(ChartTreeNodeDto.to_json())

# convert the object into a dict
chart_tree_node_dto_dict = chart_tree_node_dto_instance.to_dict()
# create an instance of ChartTreeNodeDto from a dict
chart_tree_node_dto_from_dict = ChartTreeNodeDto.from_dict(chart_tree_node_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


