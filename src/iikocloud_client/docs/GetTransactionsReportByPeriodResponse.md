# GetTransactionsReportByPeriodResponse

Get transactions report by period response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | Page number. Zero based. | [optional] 
**page_size** | **int** | Page size. | [optional] 
**transactions** | [**List[TransportTransactionsReportItem]**](TransportTransactionsReportItem.md) | Transactions. | [optional] 

## Example

```python
from iikocloud_client.models.get_transactions_report_by_period_response import GetTransactionsReportByPeriodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsReportByPeriodResponse from a JSON string
get_transactions_report_by_period_response_instance = GetTransactionsReportByPeriodResponse.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsReportByPeriodResponse.to_json())

# convert the object into a dict
get_transactions_report_by_period_response_dict = get_transactions_report_by_period_response_instance.to_dict()
# create an instance of GetTransactionsReportByPeriodResponse from a dict
get_transactions_report_by_period_response_from_dict = GetTransactionsReportByPeriodResponse.from_dict(get_transactions_report_by_period_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


