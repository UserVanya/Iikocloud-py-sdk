# AccountGetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account UUID. string (UUID) | 

## Example

```python
from iikocloud_client.models.account_get_request import AccountGetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGetRequest from a JSON string
account_get_request_instance = AccountGetRequest.from_json(json)
# print the JSON string representation of the object
print(AccountGetRequest.to_json())

# convert the object into a dict
account_get_request_dict = account_get_request_instance.to_dict()
# create an instance of AccountGetRequest from a dict
account_get_request_from_dict = AccountGetRequest.from_dict(account_get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


