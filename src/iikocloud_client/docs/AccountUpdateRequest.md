# AccountUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Account code | [optional] 
**description** | **str** | Account description | 
**id** | **str** | Account UUID. string (UUID) | 
**name** | **str** | Display name | 
**parent_id** | **str** | Parent account UUID | [optional] 
**start_balance_date** | **str** | Start balance date (YYYY-MM-DD format) | 
**start_balance_sum** | **float** | Start balance amount | 
**type** | **str** | Account type code | 

## Example

```python
from iikocloud_client.models.account_update_request import AccountUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUpdateRequest from a JSON string
account_update_request_instance = AccountUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AccountUpdateRequest.to_json())

# convert the object into a dict
account_update_request_dict = account_update_request_instance.to_dict()
# create an instance of AccountUpdateRequest from a dict
account_update_request_from_dict = AccountUpdateRequest.from_dict(account_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


