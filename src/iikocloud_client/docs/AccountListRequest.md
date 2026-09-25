# AccountListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[FinanceAccountsFilter]**](FinanceAccountsFilter.md) | Request filters. All filters are applied simultaneously (AND) | 
**limit** | **int** | Maximum number of records in the response. | 
**offset** | **int** | Number of records to skip from the beginning. | 

## Example

```python
from iikocloud_client.models.account_list_request import AccountListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListRequest from a JSON string
account_list_request_instance = AccountListRequest.from_json(json)
# print the JSON string representation of the object
print(AccountListRequest.to_json())

# convert the object into a dict
account_list_request_dict = account_list_request_instance.to_dict()
# create an instance of AccountListRequest from a dict
account_list_request_from_dict = AccountListRequest.from_dict(account_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


