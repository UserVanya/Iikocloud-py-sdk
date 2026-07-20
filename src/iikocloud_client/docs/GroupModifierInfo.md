# GroupModifierInfo

Information on group of modifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_modifiers** | [**List[ChildModifierInfo]**](ChildModifierInfo.md) | List of child modifiers. | 
**child_modifiers_have_min_max_restrictions** | **bool** | Presence of max/min quantity limitations of child modifiers. | [optional] 
**default_amount** | **int** | Amount by default. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**free_of_charge_amount** | **int** | Free amount. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**hide_if_default_amount** | **bool** | Hide if the amount is by default. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**id** | **UUID** | ID. | 
**max_amount** | **int** | Maximum quantity. | 
**min_amount** | **int** | Minimum quantity. | 
**required** | **bool** | Required availability. | 
**splittable** | **bool** | Modifier can be split. This field is supported since 7.2.4 iikoRMS version. | [optional] 

## Example

```python
from iikocloud_client.models.group_modifier_info import GroupModifierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GroupModifierInfo from a JSON string
group_modifier_info_instance = GroupModifierInfo.from_json(json)
# print the JSON string representation of the object
print(GroupModifierInfo.to_json())

# convert the object into a dict
group_modifier_info_dict = group_modifier_info_instance.to_dict()
# create an instance of GroupModifierInfo from a dict
group_modifier_info_from_dict = GroupModifierInfo.from_dict(group_modifier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


