# ReportGetTransactionsReportByPeriodRequest

Report request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id. | 
**date_from** | **str** | Report since date in UTC. Included. | 
**date_to** | **str** | Report till date in UTC. Included. | 
**page_number** | **int** | Page number. Zero based. Previous pages will be skipped. | 
**page_size** | **int** | Page size. Ignored if more than max page size on server. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.report_get_transactions_report_by_period_request import ReportGetTransactionsReportByPeriodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGetTransactionsReportByPeriodRequest from a JSON string
report_get_transactions_report_by_period_request_instance = ReportGetTransactionsReportByPeriodRequest.from_json(json)
# print the JSON string representation of the object
print(ReportGetTransactionsReportByPeriodRequest.to_json())

# convert the object into a dict
report_get_transactions_report_by_period_request_dict = report_get_transactions_report_by_period_request_instance.to_dict()
# create an instance of ReportGetTransactionsReportByPeriodRequest from a dict
report_get_transactions_report_by_period_request_from_dict = ReportGetTransactionsReportByPeriodRequest.from_dict(report_get_transactions_report_by_period_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


