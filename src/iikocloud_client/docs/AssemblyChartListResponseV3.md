# AssemblyChartListResponseV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of records before limit/offset is applied | [optional] 
**deleted_assembly_chart_ids** | **List[str]** | UUIDs of assembly charts deleted since the last synchronization (relevant with knownRevision) | [optional] 
**items** | [**List[AssemblyChartResponseV3]**](AssemblyChartResponseV3.md) | Ingredient lines of the assembly chart | [optional] 
**known_revision** | **int** | Known revision for incremental synchronization (getAllUpdate). Cannot be combined with productId | [optional] 
**prepared_charts** | [**List[PreparedChartDtoV3]**](PreparedChartDtoV3.md) | Breakdown of assembly charts to store items (populated when includePreparedCharts: true) | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_list_response_v3 import AssemblyChartListResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartListResponseV3 from a JSON string
assembly_chart_list_response_v3_instance = AssemblyChartListResponseV3.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartListResponseV3.to_json())

# convert the object into a dict
assembly_chart_list_response_v3_dict = assembly_chart_list_response_v3_instance.to_dict()
# create an instance of AssemblyChartListResponseV3 from a dict
assembly_chart_list_response_v3_from_dict = AssemblyChartListResponseV3.from_dict(assembly_chart_list_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


