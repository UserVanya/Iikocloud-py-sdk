# AssemblyChartCommonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the assembly chart | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartCommonResponse from a JSON string
assembly_chart_common_response_instance = AssemblyChartCommonResponse.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartCommonResponse.to_json())

# convert the object into a dict
assembly_chart_common_response_dict = assembly_chart_common_response_instance.to_dict()
# create an instance of AssemblyChartCommonResponse from a dict
assembly_chart_common_response_from_dict = AssemblyChartCommonResponse.from_dict(assembly_chart_common_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


