# NetReportGetTransactionsReportByRevisionResponse

Get transactions report by revision response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[NetReportTransportTransactionsReportItem]**](NetReportTransportTransactionsReportItem.md) | Transactions. | [optional] 
**last_revision** | **int** | Last known transaction revision. | [optional] 
**last_transaction_id** | **str** | Last known transaction id. | [optional] 
**page_size** | **int** | Page size. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_report_get_transactions_report_by_revision_response import NetReportGetTransactionsReportByRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetReportGetTransactionsReportByRevisionResponse from a JSON string
net_report_get_transactions_report_by_revision_response_instance = NetReportGetTransactionsReportByRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(NetReportGetTransactionsReportByRevisionResponse.to_json())

# convert the object into a dict
net_report_get_transactions_report_by_revision_response_dict = net_report_get_transactions_report_by_revision_response_instance.to_dict()
# create an instance of NetReportGetTransactionsReportByRevisionResponse from a dict
net_report_get_transactions_report_by_revision_response_from_dict = NetReportGetTransactionsReportByRevisionResponse.from_dict(net_report_get_transactions_report_by_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


