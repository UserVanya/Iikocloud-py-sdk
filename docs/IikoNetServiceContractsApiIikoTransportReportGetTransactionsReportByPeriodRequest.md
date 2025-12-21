# IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest

Report request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**date_from** | **str** | Report since date in UTC. Included. | 
**date_to** | **str** | Report till date in UTC. Included. | 
**page_number** | **int** | Page number. Zero based. Previous pages will be skipped. | 
**page_size** | **int** | Page size. Ignored if more than max page size on server. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request_instance = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request_dict = iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest from a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request_from_dict = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


