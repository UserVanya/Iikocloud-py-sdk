# AccountPostingListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Financial account UUID. string (UUID) | [optional] 
**counteragent_id** | **str** | Filter by counteragent UUID. string (UUID), nullable | [optional] 
**var_from** | **str** | Period start date (YYYY-MM-DD) | [optional] 
**organization_ids** | **List[str]** | List of organization UUIDs to filter by. string[] (UUID) | [optional] 
**to** | **str** | Period end date (YYYY-MM-DD) | [optional] 

## Example

```python
from iikocloud_client.models.account_posting_list_request import AccountPostingListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPostingListRequest from a JSON string
account_posting_list_request_instance = AccountPostingListRequest.from_json(json)
# print the JSON string representation of the object
print(AccountPostingListRequest.to_json())

# convert the object into a dict
account_posting_list_request_dict = account_posting_list_request_instance.to_dict()
# create an instance of AccountPostingListRequest from a dict
account_posting_list_request_from_dict = AccountPostingListRequest.from_dict(account_posting_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


