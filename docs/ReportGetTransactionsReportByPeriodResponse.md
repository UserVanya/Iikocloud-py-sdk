# ReportGetTransactionsReportByPeriodResponse

Get transactions report by period response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[ReportTransportTransactionsReportItem]**](ReportTransportTransactionsReportItem.md) | Transactions. | [optional] 
**page_size** | **int** | Page size. | [optional] 
**page_number** | **int** | Page number. Zero based. | [optional] 

## Example

```python
from iikocloud_client.models.report_get_transactions_report_by_period_response import ReportGetTransactionsReportByPeriodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGetTransactionsReportByPeriodResponse from a JSON string
report_get_transactions_report_by_period_response_instance = ReportGetTransactionsReportByPeriodResponse.from_json(json)
# print the JSON string representation of the object
print(ReportGetTransactionsReportByPeriodResponse.to_json())

# convert the object into a dict
report_get_transactions_report_by_period_response_dict = report_get_transactions_report_by_period_response_instance.to_dict()
# create an instance of ReportGetTransactionsReportByPeriodResponse from a dict
report_get_transactions_report_by_period_response_from_dict = ReportGetTransactionsReportByPeriodResponse.from_dict(report_get_transactions_report_by_period_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


