# AccountTransactionsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account ID. string (UUID). Required | 
**var_from** | **str** | Period start date (YYYY-MM-DD format) | 
**organization_id** | **str** | Organization identifier (GUID) | 
**to** | **str** | Period end date (YYYY-MM-DD format) | 

## Example

```python
from iikocloud_client.models.account_transactions_list_request import AccountTransactionsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsListRequest from a JSON string
account_transactions_list_request_instance = AccountTransactionsListRequest.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsListRequest.to_json())

# convert the object into a dict
account_transactions_list_request_dict = account_transactions_list_request_instance.to_dict()
# create an instance of AccountTransactionsListRequest from a dict
account_transactions_list_request_from_dict = AccountTransactionsListRequest.from_dict(account_transactions_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


