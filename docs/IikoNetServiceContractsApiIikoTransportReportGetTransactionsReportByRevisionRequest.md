# IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest

Report request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**revision** | **int** | Report since revision. Included if LastTransactionId set.. | [optional] 
**last_transaction_id** | **UUID** | Report since transaction. Excluded. Can&#39;t be used without revision.. | [optional] 
**page_size** | **int** | Page size. Ignored if more than max size on server.. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request_instance = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request_dict = iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest from a dict
iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request_from_dict = IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


