# IncomePlanItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date for which the plan is set | [optional] 
**plan_value** | **float** | Planned value: amount for ABSOLUTE, percentage for PERCENT, or automatically calculated value for AUTOMATIC | [optional] 
**value_type** | **str** | Value type: ABSOLUTE — amount, PERCENT — percentage, AUTOMATIC — automatic calculation | [optional] 

## Example

```python
from iikocloud_client.models.income_plan_item import IncomePlanItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomePlanItem from a JSON string
income_plan_item_instance = IncomePlanItem.from_json(json)
# print the JSON string representation of the object
print(IncomePlanItem.to_json())

# convert the object into a dict
income_plan_item_dict = income_plan_item_instance.to_dict()
# create an instance of IncomePlanItem from a dict
income_plan_item_from_dict = IncomePlanItem.from_dict(income_plan_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


