# AccountCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Account code | [optional] 
**description** | **str** | Account description | 
**is_custom_transactions_allowed** | **bool** | Whether custom transactions are allowed for the account | [optional] 
**name** | **str** | Display name | 
**parent_id** | **str** | Parent account UUID | [optional] 
**start_balance_date** | **str** | Start balance date (YYYY-MM-DD format) | 
**start_balance_sum** | **float** | Start balance amount | 
**type** | **str** | Account type code | 

## Example

```python
from iikocloud_client.models.account_create_request import AccountCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCreateRequest from a JSON string
account_create_request_instance = AccountCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AccountCreateRequest.to_json())

# convert the object into a dict
account_create_request_dict = account_create_request_instance.to_dict()
# create an instance of AccountCreateRequest from a dict
account_create_request_from_dict = AccountCreateRequest.from_dict(account_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


