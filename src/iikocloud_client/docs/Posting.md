# Posting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_amount** | **float** | Cumulative account balance after posting. decimal | [optional] 
**can_edit** | **bool** | Whether the posting can be edited | [optional] 
**cash_flow_category_id** | **str** | Cash flow category UUID. string (UUID), nullable | [optional] 
**cash_order_number** | **str** | Cash order number. string, nullable | [optional] 
**comment** | **str** | Posting comment. string, nullable | [optional] 
**conception_id** | **str** | Conception UUID. string (UUID), nullable | [optional] 
**corresponding_account_id** | **str** | Corresponding account UUID. string (UUID) | [optional] 
**counteragent_id** | **str** | Counteragent UUID. string (UUID), nullable | [optional] 
**created_at** | **str** | Creation date and time. string, nullable | [optional] 
**department_id** | **str** | Department UUID. string (UUID), nullable | [optional] 
**document_at** | **str** | Document date (YYYY-MM-DD) | [optional] 
**document_id** | **str** | Document UUID. string (UUID), nullable | [optional] 
**document_number** | **str** | Document number. string, nullable | [optional] 
**is_credit_side** | **bool** | Credit side flag (true &#x3D; credit, false &#x3D; debit) | [optional] 
**modified_at** | **str** | Last modification date and time. string, nullable | [optional] 
**modified_by_user_id** | **str** | UUID of the user who last modified the posting. string (UUID), nullable | [optional] 
**posted_at** | **str** | Actual posting date. string (YYYY-MM-DD), nullable | [optional] 
**posting_amount** | **float** | Posting amount. decimal | [optional] 
**posting_id** | **str** | Posting UUID. string (UUID) | [optional] 
**posting_type** | **str** | Posting type (ENUM) | [optional] 
**secondary_counteragent_id** | **str** | Secondary counteragent UUID. string (UUID), nullable | [optional] 

## Example

```python
from iikocloud_client.models.posting import Posting

# TODO update the JSON string below
json = "{}"
# create an instance of Posting from a JSON string
posting_instance = Posting.from_json(json)
# print the JSON string representation of the object
print(Posting.to_json())

# convert the object into a dict
posting_dict = posting_instance.to_dict()
# create an instance of Posting from a dict
posting_from_dict = Posting.from_dict(posting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


