# GetOlapReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** | Linear report data (row by row) | [optional] 
**summary** | **List[object]** | Intermediate and grand totals of the report | [optional] 

## Example

```python
from iikocloud_client.models.get_olap_report_response import GetOlapReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOlapReportResponse from a JSON string
get_olap_report_response_instance = GetOlapReportResponse.from_json(json)
# print the JSON string representation of the object
print(GetOlapReportResponse.to_json())

# convert the object into a dict
get_olap_report_response_dict = get_olap_report_response_instance.to_dict()
# create an instance of GetOlapReportResponse from a dict
get_olap_report_response_from_dict = GetOlapReportResponse.from_dict(get_olap_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


