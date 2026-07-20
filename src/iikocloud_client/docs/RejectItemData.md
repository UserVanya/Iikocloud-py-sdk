# RejectItemData

Reject additional information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_week_days** | **List[str]** | Allowed week days. | [optional] 
**date_from** | **str** | Point work time start. | [optional] 
**date_to** | **str** | Point work time end. | [optional] 
**min_sum** | **float** | Order min sum. | [optional] 

## Example

```python
from iikocloud_client.models.reject_item_data import RejectItemData

# TODO update the JSON string below
json = "{}"
# create an instance of RejectItemData from a JSON string
reject_item_data_instance = RejectItemData.from_json(json)
# print the JSON string representation of the object
print(RejectItemData.to_json())

# convert the object into a dict
reject_item_data_dict = reject_item_data_instance.to_dict()
# create an instance of RejectItemData from a dict
reject_item_data_from_dict = RejectItemData.from_dict(reject_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


