# ChartTreeNodeDtoV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the ingredient in the parent node&#39;s composition | [optional] 
**assembled_amount** | **float** | Bookmark rate of the semi-finished product that has its own assembly chart | [optional] 
**children** | [**List[ChartTreeNodeDtoV3]**](ChartTreeNodeDtoV3.md) | Child nodes of the tree — ingredients of the assembly chart, each recursively expanded with its own composition (if it has an assembly chart) | [optional] 
**product_id** | **UUID** | UUID of the ingredient or semi-finished product | [optional] 
**product_size_specification** | **UUID** | UUID of the product size this ingredient applies to. null — applies to all sizes | [optional] 

## Example

```python
from iikocloud_client.models.chart_tree_node_dto_v3 import ChartTreeNodeDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of ChartTreeNodeDtoV3 from a JSON string
chart_tree_node_dto_v3_instance = ChartTreeNodeDtoV3.from_json(json)
# print the JSON string representation of the object
print(ChartTreeNodeDtoV3.to_json())

# convert the object into a dict
chart_tree_node_dto_v3_dict = chart_tree_node_dto_v3_instance.to_dict()
# create an instance of ChartTreeNodeDtoV3 from a dict
chart_tree_node_dto_v3_from_dict = ChartTreeNodeDtoV3.from_dict(chart_tree_node_dto_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


