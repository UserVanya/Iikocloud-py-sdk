# BalanceSheetListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_at** | **str** | Date to retrieve balances for (YYYY-MM-DD) | [optional] 
**organization_ids** | **List[str]** | List of organization UUIDs to filter by. string[] (UUID) | [optional] 

## Example

```python
from iikocloud_client.models.balance_sheet_list_request import BalanceSheetListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSheetListRequest from a JSON string
balance_sheet_list_request_instance = BalanceSheetListRequest.from_json(json)
# print the JSON string representation of the object
print(BalanceSheetListRequest.to_json())

# convert the object into a dict
balance_sheet_list_request_dict = balance_sheet_list_request_instance.to_dict()
# create an instance of BalanceSheetListRequest from a dict
balance_sheet_list_request_from_dict = BalanceSheetListRequest.from_dict(balance_sheet_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


