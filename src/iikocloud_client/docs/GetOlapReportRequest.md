# GetOlapReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_fields** | **List[str]** | Fields to aggregate by (&#x60;FieldName&#x60; names from &#x60;columns/get&#x60;) | 
**build_summary** | **bool** | Whether to build totals | [optional] 
**filters** | [**List[OlapFilterDoc]**](OlapFilterDoc.md) | Report filters: an array of filter structures; each contains name (&#x60;FieldName&#x60; from &#x60;columns/get&#x60;) and &#x60;filterType&#x60;, remaining fields depend on filterType (see filter models); at least one &#x60;DateRange&#x60; filter by the &#x60;OpenDate.Typed&#x60; field is required. For periodType &#x3D; CUSTOM the period is limited to 31 days inclusive. | 
**group_by_col_fields** | **List[str]** | Fields to group columns by (&#x60;FieldName&#x60; names from &#x60;columns/get&#x60;) | [optional] 
**group_by_row_fields** | **List[str]** | Fields to group rows by (&#x60;FieldName&#x60; names from &#x60;columns/get&#x60;) | [optional] 
**report_type** | **str** | Report type: &#x60;SALES&#x60; — sales, &#x60;TRANSACTIONS&#x60; — transactions, &#x60;DELIVERIES&#x60; — deliveries | 

## Example

```python
from iikocloud_client.models.get_olap_report_request import GetOlapReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOlapReportRequest from a JSON string
get_olap_report_request_instance = GetOlapReportRequest.from_json(json)
# print the JSON string representation of the object
print(GetOlapReportRequest.to_json())

# convert the object into a dict
get_olap_report_request_dict = get_olap_report_request_instance.to_dict()
# create an instance of GetOlapReportRequest from a dict
get_olap_report_request_from_dict = GetOlapReportRequest.from_dict(get_olap_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


