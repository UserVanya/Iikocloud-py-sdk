# NetReportGetTransactionsReportByRevisionRequest

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
from iikocloud_client.models.net_report_get_transactions_report_by_revision_request import NetReportGetTransactionsReportByRevisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetReportGetTransactionsReportByRevisionRequest from a JSON string
net_report_get_transactions_report_by_revision_request_instance = NetReportGetTransactionsReportByRevisionRequest.from_json(json)
# print the JSON string representation of the object
print(NetReportGetTransactionsReportByRevisionRequest.to_json())

# convert the object into a dict
net_report_get_transactions_report_by_revision_request_dict = net_report_get_transactions_report_by_revision_request_instance.to_dict()
# create an instance of NetReportGetTransactionsReportByRevisionRequest from a dict
net_report_get_transactions_report_by_revision_request_from_dict = NetReportGetTransactionsReportByRevisionRequest.from_dict(net_report_get_transactions_report_by_revision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


