# AccountDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account UUID. string (UUID) | 

## Example

```python
from iikocloud_client.models.account_delete_request import AccountDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDeleteRequest from a JSON string
account_delete_request_instance = AccountDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(AccountDeleteRequest.to_json())

# convert the object into a dict
account_delete_request_dict = account_delete_request_instance.to_dict()
# create an instance of AccountDeleteRequest from a dict
account_delete_request_from_dict = AccountDeleteRequest.from_dict(account_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


