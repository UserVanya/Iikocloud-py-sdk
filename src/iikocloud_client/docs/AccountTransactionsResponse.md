# AccountTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TransactionItem]**](TransactionItem.md) | Array of transactions | [optional] 
**start_balance** | **float** | Opening (incoming) account balance at the start of the period. decimal | [optional] 
**sum_total** | **float** | Total amount of all transactions in the selection. decimal | [optional] 

## Example

```python
from iikocloud_client.models.account_transactions_response import AccountTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransactionsResponse from a JSON string
account_transactions_response_instance = AccountTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountTransactionsResponse.to_json())

# convert the object into a dict
account_transactions_response_dict = account_transactions_response_instance.to_dict()
# create an instance of AccountTransactionsResponse from a dict
account_transactions_response_from_dict = AccountTransactionsResponse.from_dict(account_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


