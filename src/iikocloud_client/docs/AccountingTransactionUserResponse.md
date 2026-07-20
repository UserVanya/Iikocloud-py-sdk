# AccountingTransactionUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_transaction_id** | **str** | Transaction identifier | [optional] 
**message** | **str** | Operation result message | [optional] 
**organization_id** | **str** | Organization identifier | [optional] 

## Example

```python
from iikocloud_client.models.accounting_transaction_user_response import AccountingTransactionUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingTransactionUserResponse from a JSON string
accounting_transaction_user_response_instance = AccountingTransactionUserResponse.from_json(json)
# print the JSON string representation of the object
print(AccountingTransactionUserResponse.to_json())

# convert the object into a dict
accounting_transaction_user_response_dict = accounting_transaction_user_response_instance.to_dict()
# create an instance of AccountingTransactionUserResponse from a dict
accounting_transaction_user_response_from_dict = AccountingTransactionUserResponse.from_dict(accounting_transaction_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


