# NetReportGetTransactionsReportByPeriodResponse

Get transactions report by period response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[NetReportTransportTransactionsReportItem]**](NetReportTransportTransactionsReportItem.md) | Transactions. | [optional] 
**page_size** | **int** | Page size. | [optional] 
**page_number** | **int** | Page number. Zero based. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_report_get_transactions_report_by_period_response import NetReportGetTransactionsReportByPeriodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetReportGetTransactionsReportByPeriodResponse from a JSON string
net_report_get_transactions_report_by_period_response_instance = NetReportGetTransactionsReportByPeriodResponse.from_json(json)
# print the JSON string representation of the object
print(NetReportGetTransactionsReportByPeriodResponse.to_json())

# convert the object into a dict
net_report_get_transactions_report_by_period_response_dict = net_report_get_transactions_report_by_period_response_instance.to_dict()
# create an instance of NetReportGetTransactionsReportByPeriodResponse from a dict
net_report_get_transactions_report_by_period_response_from_dict = NetReportGetTransactionsReportByPeriodResponse.from_dict(net_report_get_transactions_report_by_period_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


