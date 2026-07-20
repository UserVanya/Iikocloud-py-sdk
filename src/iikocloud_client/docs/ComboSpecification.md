# ComboSpecification

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **UUID** | Combo&#39;s category id. | [optional] 
**expiration_date** | **str** | Expiration date. | [optional] 
**groups** | [**List[ComboGroup]**](ComboGroup.md) | Groups. | [optional] 
**include_modifiers** | **bool** | Include modifiers. | [optional] 
**is_active** | **bool** | Is active. | [optional] 
**lacking_groups_to_suggest** | **int** | Lacking groups to suggest. | [optional] 
**name** | **str** | Name. Can be null. | [optional] 
**price_modification** | **float** | Price modification. | [optional] 
**price_modification_type** | [**ComboPriceModificationType**](ComboPriceModificationType.md) | Price modification type.  &lt;br&gt;0 - fixed combo price,&lt;br /&gt;1 - fixed position price,&lt;br /&gt;2 - cheapest position discount,&lt;br /&gt;3 - most expensive position discount,&lt;br /&gt;4 - percentage discount for each position. | [optional] 
**sort_order** | **int** | Sort order. | [optional] 
**source_action_id** | **UUID** | Id of action that added the combo. | [optional] 
**start_date** | **str** | Start date. | [optional] 

## Example

```python
from iikocloud_client.models.combo_specification import ComboSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ComboSpecification from a JSON string
combo_specification_instance = ComboSpecification.from_json(json)
# print the JSON string representation of the object
print(ComboSpecification.to_json())

# convert the object into a dict
combo_specification_dict = combo_specification_instance.to_dict()
# create an instance of ComboSpecification from a dict
combo_specification_from_dict = ComboSpecification.from_dict(combo_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


