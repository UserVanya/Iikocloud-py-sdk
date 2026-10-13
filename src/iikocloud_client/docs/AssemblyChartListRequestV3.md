# AssemblyChartListRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Start of the sample period (YYYY-MM-DD). Required when the product filter is not set | [optional] 
**date_to** | **str** | End of the sample period (YYYY-MM-DD). Optional | [optional] 
**filters** | [**List[AssemblyChartV3Filter]**](AssemblyChartV3Filter.md) | List filters. Supported fields are product (eq/in) and department (eq/in); without a product filter all charts for the period are returned | [optional] 
**include_deleted_products** | **bool** | Whether to include assembly charts of deleted products. Defaults to true | [optional] 
**include_prepared_charts** | **bool** | Whether to include the breakdown to store items (preparedCharts) in the response. Defaults to false | [optional] 
**known_revision** | **int** | Known revision for incremental synchronization. Cannot be combined with the product filter | [optional] 
**limit** | **int** | Page size. Not set or &lt;&#x3D; 0 — no limit | [optional] 
**offset** | **int** | Offset from the start of the list. Defaults to 0 | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_list_request_v3 import AssemblyChartListRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartListRequestV3 from a JSON string
assembly_chart_list_request_v3_instance = AssemblyChartListRequestV3.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartListRequestV3.to_json())

# convert the object into a dict
assembly_chart_list_request_v3_dict = assembly_chart_list_request_v3_instance.to_dict()
# create an instance of AssemblyChartListRequestV3 from a dict
assembly_chart_list_request_v3_from_dict = AssemblyChartListRequestV3.from_dict(assembly_chart_list_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


