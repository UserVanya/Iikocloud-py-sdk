# ResolveResponseV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembled** | [**AssemblyChartResponseV3**](AssemblyChartResponseV3.md) | Top-level assembly chart (view: assembled) | [optional] 
**prepared** | [**PreparedChartDtoV3**](PreparedChartDtoV3.md) | Breakdown of the assembly chart to store items (view: prepared) | [optional] 
**tree** | [**ChartTreeNodeDtoV3**](ChartTreeNodeDtoV3.md) | Recipe tree (view: tree) | [optional] 
**view** | **str** | Chart representation: assembled — top-level chart, prepared — breakdown to store items, tree — recipe tree | [optional] 

## Example

```python
from iikocloud_client.models.resolve_response_v3 import ResolveResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveResponseV3 from a JSON string
resolve_response_v3_instance = ResolveResponseV3.from_json(json)
# print the JSON string representation of the object
print(ResolveResponseV3.to_json())

# convert the object into a dict
resolve_response_v3_dict = resolve_response_v3_instance.to_dict()
# create an instance of ResolveResponseV3 from a dict
resolve_response_v3_from_dict = ResolveResponseV3.from_dict(resolve_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


