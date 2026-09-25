# AccountPostingListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Financial account UUID. string (UUID) | [optional] 
**can_edit** | **bool** | Whether postings can be edited | [optional] 
**opening_balance_amount** | **float** | Opening balance at the start of the period. decimal | [optional] 
**period_change_amount** | **float** | Net change in balance over the period. decimal | [optional] 
**postings** | [**List[Posting]**](Posting.md) | List of postings | [optional] 

## Example

```python
from iikocloud_client.models.account_posting_list_response import AccountPostingListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPostingListResponse from a JSON string
account_posting_list_response_instance = AccountPostingListResponse.from_json(json)
# print the JSON string representation of the object
print(AccountPostingListResponse.to_json())

# convert the object into a dict
account_posting_list_response_dict = account_posting_list_response_instance.to_dict()
# create an instance of AccountPostingListResponse from a dict
account_posting_list_response_from_dict = AccountPostingListResponse.from_dict(account_posting_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


