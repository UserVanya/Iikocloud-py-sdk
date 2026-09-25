# AccountRestoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account UUID. string (UUID) | [optional] 
**is_deleted** | **bool** | Deleted flag | [optional] 
**restore_descendants** | **bool** | Flag to restore child accounts | [optional] 

## Example

```python
from iikocloud_client.models.account_restore_response import AccountRestoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRestoreResponse from a JSON string
account_restore_response_instance = AccountRestoreResponse.from_json(json)
# print the JSON string representation of the object
print(AccountRestoreResponse.to_json())

# convert the object into a dict
account_restore_response_dict = account_restore_response_instance.to_dict()
# create an instance of AccountRestoreResponse from a dict
account_restore_response_from_dict = AccountRestoreResponse.from_dict(account_restore_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


