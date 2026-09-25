# CashFlowCategoryRestoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Cash flow category UUID. string (UUID) | 
**restore_descendants** | **bool** | Flag to restore child accounts | 

## Example

```python
from iikocloud_client.models.cash_flow_category_restore_request import CashFlowCategoryRestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategoryRestoreRequest from a JSON string
cash_flow_category_restore_request_instance = CashFlowCategoryRestoreRequest.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategoryRestoreRequest.to_json())

# convert the object into a dict
cash_flow_category_restore_request_dict = cash_flow_category_restore_request_instance.to_dict()
# create an instance of CashFlowCategoryRestoreRequest from a dict
cash_flow_category_restore_request_from_dict = CashFlowCategoryRestoreRequest.from_dict(cash_flow_category_restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


