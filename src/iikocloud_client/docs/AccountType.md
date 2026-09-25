# AccountType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Account type code | [optional] 
**title** | **str** | Account type title | [optional] 

## Example

```python
from iikocloud_client.models.account_type import AccountType

# TODO update the JSON string below
json = "{}"
# create an instance of AccountType from a JSON string
account_type_instance = AccountType.from_json(json)
# print the JSON string representation of the object
print(AccountType.to_json())

# convert the object into a dict
account_type_dict = account_type_instance.to_dict()
# create an instance of AccountType from a dict
account_type_from_dict = AccountType.from_dict(account_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


