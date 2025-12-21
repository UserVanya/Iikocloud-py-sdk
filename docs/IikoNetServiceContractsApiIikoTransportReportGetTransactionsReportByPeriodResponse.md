# IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse

Get transactions report by period response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[IikoNetServiceContractsApiIikoTransportReportTransportTransactionsReportItem]**](IikoNetServiceContractsApiIikoTransportReportTransportTransactionsReportItem.md) | Transactions. | [optional] 
**page_size** | **int** | Page size. | [optional] 
**page_number** | **int** | Page number. Zero based. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_response import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_response_instance = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_response_dict = iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse from a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_response_from_dict = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


