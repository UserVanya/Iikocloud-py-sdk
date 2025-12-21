# ComboGroupDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Uuid**](Uuid.md) |  | 
**name** | **str** |  | 
**is_main_group** | **bool** | Includes main dishes - these are the items around which the combo set is built. If a main dish is added to the order, the system can display a prompt &#39;build a combo set&#39;. | 
**items** | [**List[ComboGroupItemDto2]**](ComboGroupItemDto2.md) |  | [optional] 
**skip_step** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.combo_group_dto2 import ComboGroupDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupDto2 from a JSON string
combo_group_dto2_instance = ComboGroupDto2.from_json(json)
# print the JSON string representation of the object
print(ComboGroupDto2.to_json())

# convert the object into a dict
combo_group_dto2_dict = combo_group_dto2_instance.to_dict()
# create an instance of ComboGroupDto2 from a dict
combo_group_dto2_from_dict = ComboGroupDto2.from_dict(combo_group_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


