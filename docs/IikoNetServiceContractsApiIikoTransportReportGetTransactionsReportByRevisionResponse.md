# IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse

Get transactions report by revision response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[IikoNetServiceContractsApiIikoTransportReportTransportTransactionsReportItem]**](IikoNetServiceContractsApiIikoTransportReportTransportTransactionsReportItem.md) | Transactions. | [optional] 
**last_revision** | **int** | Last known transaction revision. | [optional] 
**last_transaction_id** | **UUID** | Last known transaction id. | [optional] 
**page_size** | **int** | Page size. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_response import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_response_instance = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_response_dict = iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse from a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_response_from_dict = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


