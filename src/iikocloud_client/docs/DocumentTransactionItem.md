# DocumentTransactionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_flow_category** | **str** | Cash flow category. string (UUID), or null | [optional] 
**cash_order_number** | **str** | Cash order number. string, or null | [optional] 
**comment** | **str** | Transaction comment. string, or null | [optional] 
**conception** | **str** | Concept the transaction belongs to. string (UUID), or null | [optional] 
**var_date** | **str** | Transaction accounting date and time. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm) | [optional] 
**date_created** | **str** | Transaction creation date. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm) | [optional] 
**date_modified** | **str** | Transaction last modified date. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm), or null | [optional] 
**date_secondary** | **str** | Secondary transaction date. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm), or null | [optional] 
**document_id** | **str** | Related document ID. string (UUID), or null | [optional] 
**document_item_id** | **str** | Document item ID. string (UUID), or null | [optional] 
**var_from** | [**TransactionSide**](TransactionSide.md) | Transaction FROM (debit) side | [optional] 
**id** | **str** | Transaction UUID. string (UUID) | [optional] 
**number** | **str** | Related document or cash session number. string, or null | [optional] 
**session** | **str** | Cash session in which the transaction was created. string (UUID), or null | [optional] 
**sum** | **float** | Transaction amount. decimal | [optional] 
**to** | [**TransactionSide**](TransactionSide.md) | Transaction TO (credit) side | [optional] 
**type** | **str** | Transaction type, ENUM | [optional] 
**user_modified** | **str** | User who last modified the transaction. string (UUID), or null | [optional] 

## Example

```python
from iikocloud_client.models.document_transaction_item import DocumentTransactionItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTransactionItem from a JSON string
document_transaction_item_instance = DocumentTransactionItem.from_json(json)
# print the JSON string representation of the object
print(DocumentTransactionItem.to_json())

# convert the object into a dict
document_transaction_item_dict = document_transaction_item_instance.to_dict()
# create an instance of DocumentTransactionItem from a dict
document_transaction_item_from_dict = DocumentTransactionItem.from_dict(document_transaction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


