# ManualConditionInfo

Manual condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | Name of manual condition. | [optional] 
**id** | **UUID** | Id. | [optional] 
**is_applicable_on_cashier_screen** | **bool** | Flag of applicability on the cashier screen.. | [optional] 
**is_dynamic_discount** | **bool** | Arbitrary discount attribute. | [optional] 

## Example

```python
from iikocloud_client.models.manual_condition_info import ManualConditionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManualConditionInfo from a JSON string
manual_condition_info_instance = ManualConditionInfo.from_json(json)
# print the JSON string representation of the object
print(ManualConditionInfo.to_json())

# convert the object into a dict
manual_condition_info_dict = manual_condition_info_instance.to_dict()
# create an instance of ManualConditionInfo from a dict
manual_condition_info_from_dict = ManualConditionInfo.from_dict(manual_condition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


