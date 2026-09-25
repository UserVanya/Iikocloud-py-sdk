# BalanceSheetListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_at** | **str** | Date to retrieve balances for (YYYY-MM-DD) | [optional] 
**balances** | [**List[BalanceItem]**](BalanceItem.md) | List of account balances | [optional] 

## Example

```python
from iikocloud_client.models.balance_sheet_list_response import BalanceSheetListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSheetListResponse from a JSON string
balance_sheet_list_response_instance = BalanceSheetListResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceSheetListResponse.to_json())

# convert the object into a dict
balance_sheet_list_response_dict = balance_sheet_list_response_instance.to_dict()
# create an instance of BalanceSheetListResponse from a dict
balance_sheet_list_response_from_dict = BalanceSheetListResponse.from_dict(balance_sheet_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


