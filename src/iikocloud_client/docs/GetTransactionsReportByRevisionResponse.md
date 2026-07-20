# GetTransactionsReportByRevisionResponse

Get transactions report by revision response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_revision** | **int** | Last known transaction revision. | [optional] 
**last_transaction_id** | **UUID** | Last known transaction id. | [optional] 
**page_size** | **int** | Page size. | [optional] 
**transactions** | [**List[TransportTransactionsReportItem]**](TransportTransactionsReportItem.md) | Transactions. | [optional] 

## Example

```python
from iikocloud_client.models.get_transactions_report_by_revision_response import GetTransactionsReportByRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsReportByRevisionResponse from a JSON string
get_transactions_report_by_revision_response_instance = GetTransactionsReportByRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsReportByRevisionResponse.to_json())

# convert the object into a dict
get_transactions_report_by_revision_response_dict = get_transactions_report_by_revision_response_instance.to_dict()
# create an instance of GetTransactionsReportByRevisionResponse from a dict
get_transactions_report_by_revision_response_from_dict = GetTransactionsReportByRevisionResponse.from_dict(get_transactions_report_by_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


