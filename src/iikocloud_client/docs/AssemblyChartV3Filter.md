# AssemblyChartV3Filter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name for filtering | [optional] 
**op** | **str** | Comparison operator: \&quot;eq\&quot; (equal), \&quot;ne\&quot; (not equal), \&quot;gt\&quot; (greater than), \&quot;gte\&quot; (greater than or equal), \&quot;lt\&quot; (less than), \&quot;lte\&quot; (less than or equal), \&quot;in\&quot; (value in list — uses values[]), \&quot;nin\&quot; (value not in list — uses values[]), \&quot;like\&quot; (case-insensitive substring), \&quot;blank\&quot; (null or empty string), \&quot;notblank\&quot; (not null and not empty string) | [optional] 
**value** | **object** | Scalar value for filtering (used with eq, ne, gt, gte, lt, lte, like) | [optional] 
**values** | **List[object]** | Array of values for multi-value filtering (used with \&quot;in\&quot;, \&quot;nin\&quot;) | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_v3_filter import AssemblyChartV3Filter

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartV3Filter from a JSON string
assembly_chart_v3_filter_instance = AssemblyChartV3Filter.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartV3Filter.to_json())

# convert the object into a dict
assembly_chart_v3_filter_dict = assembly_chart_v3_filter_instance.to_dict()
# create an instance of AssemblyChartV3Filter from a dict
assembly_chart_v3_filter_from_dict = AssemblyChartV3Filter.from_dict(assembly_chart_v3_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


