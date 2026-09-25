# ChartOfAccountsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[ChartOfAccount]**](ChartOfAccount.md) | List of accounts | [optional] 

## Example

```python
from iikocloud_client.models.chart_of_accounts_list_response import ChartOfAccountsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccountsListResponse from a JSON string
chart_of_accounts_list_response_instance = ChartOfAccountsListResponse.from_json(json)
# print the JSON string representation of the object
print(ChartOfAccountsListResponse.to_json())

# convert the object into a dict
chart_of_accounts_list_response_dict = chart_of_accounts_list_response_instance.to_dict()
# create an instance of ChartOfAccountsListResponse from a dict
chart_of_accounts_list_response_from_dict = ChartOfAccountsListResponse.from_dict(chart_of_accounts_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


