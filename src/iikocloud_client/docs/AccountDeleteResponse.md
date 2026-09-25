# AccountDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account UUID. string (UUID) | [optional] 
**is_deleted** | **bool** | Deleted flag | [optional] 

## Example

```python
from iikocloud_client.models.account_delete_response import AccountDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDeleteResponse from a JSON string
account_delete_response_instance = AccountDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(AccountDeleteResponse.to_json())

# convert the object into a dict
account_delete_response_dict = account_delete_response_instance.to_dict()
# create an instance of AccountDeleteResponse from a dict
account_delete_response_from_dict = AccountDeleteResponse.from_dict(account_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


