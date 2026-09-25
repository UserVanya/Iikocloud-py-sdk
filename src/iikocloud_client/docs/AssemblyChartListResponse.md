# AssemblyChartListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_assembly_chart_ids** | **List[str]** | UUIDs of assembly charts deleted since the last synchronization (relevant with knownRevision) | [optional] 
**deleted_prepared_chart_ids** | **List[str]** | UUIDs of prepared charts deleted since the last synchronization (relevant with knownRevision) | [optional] 
**items** | [**List[AssemblyChartResponse]**](AssemblyChartResponse.md) | Ingredient lines of the assembly chart | [optional] 
**known_revision** | **int** | Known revision for incremental synchronization (getAllUpdate). Cannot be combined with productId | [optional] 
**prepared_charts** | [**List[PreparedChartDto]**](PreparedChartDto.md) | Breakdown of assembly charts to store items (populated when includePreparedCharts: true) | [optional] 
**total_count** | **int** | Total number of assembly charts of the product | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_list_response import AssemblyChartListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartListResponse from a JSON string
assembly_chart_list_response_instance = AssemblyChartListResponse.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartListResponse.to_json())

# convert the object into a dict
assembly_chart_list_response_dict = assembly_chart_list_response_instance.to_dict()
# create an instance of AssemblyChartListResponse from a dict
assembly_chart_list_response_from_dict = AssemblyChartListResponse.from_dict(assembly_chart_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


