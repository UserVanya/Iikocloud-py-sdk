# AccountListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[Account]**](Account.md) | List of accounts | [optional] 
**count** | **int** | Number of items returned in the response | [optional] 
**limit** | **int** | Maximum number of records in the response. | [optional] 
**offset** | **int** | Number of records to skip from the beginning. | [optional] 

## Example

```python
from iikocloud_client.models.account_list_response import AccountListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListResponse from a JSON string
account_list_response_instance = AccountListResponse.from_json(json)
# print the JSON string representation of the object
print(AccountListResponse.to_json())

# convert the object into a dict
account_list_response_dict = account_list_response_instance.to_dict()
# create an instance of AccountListResponse from a dict
account_list_response_from_dict = AccountListResponse.from_dict(account_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


