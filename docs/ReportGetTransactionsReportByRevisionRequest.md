# ReportGetTransactionsReportByRevisionRequest

Report request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id. | 
**revision** | **int** | Report since revision. Included if LastTransactionId set.. | [optional] 
**last_transaction_id** | **str** | Report since transaction. Excluded. Can&#39;t be used without revision.. | [optional] 
**page_size** | **int** | Page size. Ignored if more than max size on server.. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.report_get_transactions_report_by_revision_request import ReportGetTransactionsReportByRevisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGetTransactionsReportByRevisionRequest from a JSON string
report_get_transactions_report_by_revision_request_instance = ReportGetTransactionsReportByRevisionRequest.from_json(json)
# print the JSON string representation of the object
print(ReportGetTransactionsReportByRevisionRequest.to_json())

# convert the object into a dict
report_get_transactions_report_by_revision_request_dict = report_get_transactions_report_by_revision_request_instance.to_dict()
# create an instance of ReportGetTransactionsReportByRevisionRequest from a dict
report_get_transactions_report_by_revision_request_from_dict = ReportGetTransactionsReportByRevisionRequest.from_dict(report_get_transactions_report_by_revision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


