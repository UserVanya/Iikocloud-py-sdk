# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Account code | [optional] 
**created_at** | **str** | Creation date and time | [optional] 
**deleted_at** | **str** | Deletion date and time | [optional] 
**description** | **str** | Account description | [optional] 
**id** | **str** | Account UUID. string (UUID) | [optional] 
**is_custom_transactions_allowed** | **bool** | Whether custom transactions are allowed for the account | [optional] 
**is_deleted** | **bool** | Deleted flag | [optional] 
**is_system_account** | **bool** | Whether the account is a system account | [optional] 
**modified_at** | **str** | Last modification date and time | [optional] 
**name** | **str** | Display name | [optional] 
**parent_id** | **str** | Parent account UUID | [optional] 
**revision** | **int** | Revision | [optional] 
**start_balance_date** | **str** | Start balance date (YYYY-MM-DD format) | [optional] 
**start_balance_sum** | **float** | Start balance amount | [optional] 
**type** | **str** | Account type code | [optional] 

## Example

```python
from iikocloud_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


