# ReportGetTransactionsReportByRevisionResponse

Get transactions report by revision response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[ReportTransportTransactionsReportItem]**](ReportTransportTransactionsReportItem.md) | Transactions. | [optional] 
**last_revision** | **int** | Last known transaction revision. | [optional] 
**last_transaction_id** | **str** | Last known transaction id. | [optional] 
**page_size** | **int** | Page size. | [optional] 

## Example

```python
from iikocloud_client.models.report_get_transactions_report_by_revision_response import ReportGetTransactionsReportByRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGetTransactionsReportByRevisionResponse from a JSON string
report_get_transactions_report_by_revision_response_instance = ReportGetTransactionsReportByRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(ReportGetTransactionsReportByRevisionResponse.to_json())

# convert the object into a dict
report_get_transactions_report_by_revision_response_dict = report_get_transactions_report_by_revision_response_instance.to_dict()
# create an instance of ReportGetTransactionsReportByRevisionResponse from a dict
report_get_transactions_report_by_revision_response_from_dict = ReportGetTransactionsReportByRevisionResponse.from_dict(report_get_transactions_report_by_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


