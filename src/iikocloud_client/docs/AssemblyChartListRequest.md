# AssemblyChartListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Start of the sample period (YYYY-MM-DD). Required when productId is not set, or when knownRevision is set | [optional] 
**date_to** | **str** | End of the sample period (YYYY-MM-DD). Optional | [optional] 
**include_deleted_products** | **bool** | Whether to include assembly charts of deleted products. Defaults to true | [optional] 
**include_prepared_charts** | **bool** | Whether to include the breakdown to store items (preparedCharts) in the response. Defaults to false | [optional] 
**known_revision** | **int** | Known revision for incremental synchronization (getAllUpdate). Cannot be combined with productId | [optional] 
**product_id** | **UUID** | UUID of the product to retrieve assembly charts for | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_list_request import AssemblyChartListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartListRequest from a JSON string
assembly_chart_list_request_instance = AssemblyChartListRequest.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartListRequest.to_json())

# convert the object into a dict
assembly_chart_list_request_dict = assembly_chart_list_request_instance.to_dict()
# create an instance of AssemblyChartListRequest from a dict
assembly_chart_list_request_from_dict = AssemblyChartListRequest.from_dict(assembly_chart_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


