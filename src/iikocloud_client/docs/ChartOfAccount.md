# ChartOfAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_group** | **str** | Account group: ASSETS, LIABILITIES, EQUITY, INCOME_EXPENSES | [optional] 
**account_type** | **str** | Account type (ENUM) | [optional] 
**code** | **str** | Account code | [optional] 
**description** | **str** | Account description | [optional] 
**id** | **str** | Account UUID. string (UUID) | [optional] 
**is_custom_transactions_allowed** | **bool** | Whether custom transactions are allowed for the account | [optional] 
**is_deleted** | **bool** | Deletion flag | [optional] 
**is_system_account** | **bool** | Whether the account is a system account | [optional] 
**name** | **str** | Display name | [optional] 
**parent_account_id** | **str** | Parent account UUID. string (UUID), nullable | [optional] 

## Example

```python
from iikocloud_client.models.chart_of_account import ChartOfAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccount from a JSON string
chart_of_account_instance = ChartOfAccount.from_json(json)
# print the JSON string representation of the object
print(ChartOfAccount.to_json())

# convert the object into a dict
chart_of_account_dict = chart_of_account_instance.to_dict()
# create an instance of ChartOfAccount from a dict
chart_of_account_from_dict = ChartOfAccount.from_dict(chart_of_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


