# CashFlowCategoryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Cash flow category code | 
**id** | **str** | Cash flow category UUID. string (UUID) | 
**name** | **str** | Display name | 
**parent_id** | **str** | Parent cash flow category UUID | [optional] 
**type** | **str** | Cash flow category type. Allowed values: &#x60;FINANCE&#x60;, &#x60;INVESTMENT&#x60;, &#x60;OPERATIONAL&#x60; | 

## Example

```python
from iikocloud_client.models.cash_flow_category_update_request import CashFlowCategoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategoryUpdateRequest from a JSON string
cash_flow_category_update_request_instance = CashFlowCategoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategoryUpdateRequest.to_json())

# convert the object into a dict
cash_flow_category_update_request_dict = cash_flow_category_update_request_instance.to_dict()
# create an instance of CashFlowCategoryUpdateRequest from a dict
cash_flow_category_update_request_from_dict = CashFlowCategoryUpdateRequest.from_dict(cash_flow_category_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


