# AccountRestoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account UUID. string (UUID) | 
**restore_descendants** | **bool** | Flag to restore child accounts | 

## Example

```python
from iikocloud_client.models.account_restore_request import AccountRestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRestoreRequest from a JSON string
account_restore_request_instance = AccountRestoreRequest.from_json(json)
# print the JSON string representation of the object
print(AccountRestoreRequest.to_json())

# convert the object into a dict
account_restore_request_dict = account_restore_request_instance.to_dict()
# create an instance of AccountRestoreRequest from a dict
account_restore_request_from_dict = AccountRestoreRequest.from_dict(account_restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


