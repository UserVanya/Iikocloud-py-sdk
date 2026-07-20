# TransactionSide


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account or store. string (UUID) | [optional] 
**amount** | **float** | Product quantity. decimal, or null | [optional] 
**counteragent** | **str** | Counteragent. string (UUID), or null | [optional] 
**product** | **str** | Product. string (UUID), or null | [optional] 

## Example

```python
from iikocloud_client.models.transaction_side import TransactionSide

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSide from a JSON string
transaction_side_instance = TransactionSide.from_json(json)
# print the JSON string representation of the object
print(TransactionSide.to_json())

# convert the object into a dict
transaction_side_dict = transaction_side_instance.to_dict()
# create an instance of TransactionSide from a dict
transaction_side_from_dict = TransactionSide.from_dict(transaction_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


