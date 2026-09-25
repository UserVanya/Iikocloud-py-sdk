# CashFlowCategoryDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Cash flow category UUID. string (UUID) | 

## Example

```python
from iikocloud_client.models.cash_flow_category_delete_request import CashFlowCategoryDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategoryDeleteRequest from a JSON string
cash_flow_category_delete_request_instance = CashFlowCategoryDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategoryDeleteRequest.to_json())

# convert the object into a dict
cash_flow_category_delete_request_dict = cash_flow_category_delete_request_instance.to_dict()
# create an instance of CashFlowCategoryDeleteRequest from a dict
cash_flow_category_delete_request_from_dict = CashFlowCategoryDeleteRequest.from_dict(cash_flow_category_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


