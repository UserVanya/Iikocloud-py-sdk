# CashFlowCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Cash flow category code | [optional] 
**created_at** | **str** | Creation date and time | [optional] 
**deleted_at** | **str** | Deletion date and time | [optional] 
**id** | **str** | Cash flow category UUID. string (UUID) | [optional] 
**is_deleted** | **bool** | Deleted flag | [optional] 
**modified_at** | **str** | Last modification date and time | [optional] 
**name** | **str** | Display name | [optional] 
**parent_id** | **str** | Parent cash flow category UUID | [optional] 
**revision** | **int** | Revision | [optional] 
**type** | **str** | Cash flow category type. Allowed values: &#x60;FINANCE&#x60;, &#x60;INVESTMENT&#x60;, &#x60;OPERATIONAL&#x60; | [optional] 

## Example

```python
from iikocloud_client.models.cash_flow_category import CashFlowCategory

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategory from a JSON string
cash_flow_category_instance = CashFlowCategory.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategory.to_json())

# convert the object into a dict
cash_flow_category_dict = cash_flow_category_instance.to_dict()
# create an instance of CashFlowCategory from a dict
cash_flow_category_from_dict = CashFlowCategory.from_dict(cash_flow_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


