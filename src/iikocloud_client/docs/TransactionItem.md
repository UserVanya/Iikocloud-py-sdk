# TransactionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account or store. string (UUID) | [optional] 
**balance** | **float** | Accumulated account balance after this transaction. decimal | [optional] 
**cash_flow_category** | **str** | Cash flow category. string (UUID), or null | [optional] 
**cash_order_number** | **str** | Cash order number. string, or null | [optional] 
**cause_event_id** | **str** | ID of the event that caused the transaction creation. string (UUID), or &#x60;null&#x60; | [optional] 
**comment** | **str** | Transaction comment. string, or null | [optional] 
**conception** | **str** | Concept the transaction belongs to. string (UUID), or null | [optional] 
**counteragent** | **str** | Counteragent. string (UUID), or null | [optional] 
**var_date** | **str** | Transaction accounting date and time. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm) | [optional] 
**date_created** | **str** | Transaction creation date. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm) | [optional] 
**date_modified** | **str** | Transaction last modified date. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm), or null | [optional] 
**date_secondary** | **str** | Secondary transaction date. string (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm), or null | [optional] 
**document_id** | **str** | Related document ID. string (UUID), or null | [optional] 
**document_type** | **str** | Document type, ENUM | [optional] 
**number** | **str** | Related document or cash session number. string, or null | [optional] 
**penalty_or_bonus_type** | **str** | Penalty/bonus type — filled only for &#x60;PENALTY&#x60; / &#x60;BONUS&#x60; transactions. UUID, or &#x60;null&#x60; | [optional] 
**second_counteragent** | **str** | Corresponding counteragent (employee/user) for the transaction. string (UUID), or &#x60;null&#x60; | [optional] 
**session** | **str** | Cash session in which the transaction was created. string (UUID), or null | [optional] 
**sum** | **float** | Transaction amount. decimal | [optional] 
**terminal** | **str** | Terminal on which the transaction was created. string (UUID), or &#x60;null&#x60; | [optional] 
**type** | **str** | Transaction type, ENUM | [optional] 
**user_modified** | **str** | User who last modified the transaction. string (UUID), or null | [optional] 

## Example

```python
from iikocloud_client.models.transaction_item import TransactionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionItem from a JSON string
transaction_item_instance = TransactionItem.from_json(json)
# print the JSON string representation of the object
print(TransactionItem.to_json())

# convert the object into a dict
transaction_item_dict = transaction_item_instance.to_dict()
# create an instance of TransactionItem from a dict
transaction_item_from_dict = TransactionItem.from_dict(transaction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


