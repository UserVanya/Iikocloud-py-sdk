# ChartOfAccountsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** | Account type (ENUM) | [optional] 
**is_deleted** | **bool** | Deletion flag | [optional] 

## Example

```python
from iikocloud_client.models.chart_of_accounts_list_request import ChartOfAccountsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccountsListRequest from a JSON string
chart_of_accounts_list_request_instance = ChartOfAccountsListRequest.from_json(json)
# print the JSON string representation of the object
print(ChartOfAccountsListRequest.to_json())

# convert the object into a dict
chart_of_accounts_list_request_dict = chart_of_accounts_list_request_instance.to_dict()
# create an instance of ChartOfAccountsListRequest from a dict
chart_of_accounts_list_request_from_dict = ChartOfAccountsListRequest.from_dict(chart_of_accounts_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


