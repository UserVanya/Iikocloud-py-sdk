# GetTransactionsReportByRevisionRequest

Report request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**last_transaction_id** | **UUID** | Report since transaction. Excluded. Can&#39;t be used without revision.. | [optional] 
**organization_id** | **UUID** | Organization id. | 
**page_size** | **int** | Page size. Ignored if more than max size on server.. | 
**revision** | **int** | Report since revision. Included if LastTransactionId set.. | [optional] 

## Example

```python
from iikocloud_client.models.get_transactions_report_by_revision_request import GetTransactionsReportByRevisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsReportByRevisionRequest from a JSON string
get_transactions_report_by_revision_request_instance = GetTransactionsReportByRevisionRequest.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsReportByRevisionRequest.to_json())

# convert the object into a dict
get_transactions_report_by_revision_request_dict = get_transactions_report_by_revision_request_instance.to_dict()
# create an instance of GetTransactionsReportByRevisionRequest from a dict
get_transactions_report_by_revision_request_from_dict = GetTransactionsReportByRevisionRequest.from_dict(get_transactions_report_by_revision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


