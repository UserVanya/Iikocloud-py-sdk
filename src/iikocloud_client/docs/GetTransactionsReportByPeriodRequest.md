# GetTransactionsReportByPeriodRequest

Report request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**date_from** | **str** | Report since date in UTC. Included. | 
**date_to** | **str** | Report till date in UTC. Included. | 
**organization_id** | **UUID** | Organization id. | 
**page_number** | **int** | Page number. Zero based. Previous pages will be skipped. | 
**page_size** | **int** | Page size. Ignored if more than max page size on server. | 

## Example

```python
from iikocloud_client.models.get_transactions_report_by_period_request import GetTransactionsReportByPeriodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsReportByPeriodRequest from a JSON string
get_transactions_report_by_period_request_instance = GetTransactionsReportByPeriodRequest.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsReportByPeriodRequest.to_json())

# convert the object into a dict
get_transactions_report_by_period_request_dict = get_transactions_report_by_period_request_instance.to_dict()
# create an instance of GetTransactionsReportByPeriodRequest from a dict
get_transactions_report_by_period_request_from_dict = GetTransactionsReportByPeriodRequest.from_dict(get_transactions_report_by_period_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


