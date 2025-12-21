# ComboGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Uuid**](Uuid.md) |  | 
**name** | **str** |  | 
**is_main_group** | **bool** | Includes main dishes - these are the items around which the combo set is built. If a main dish is added to the order, the system can display a prompt &#39;build a combo set&#39;. | 
**items** | [**List[ComboGroupItemDto]**](ComboGroupItemDto.md) |  | [optional] 
**skip_step** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.combo_group_dto import ComboGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupDto from a JSON string
combo_group_dto_instance = ComboGroupDto.from_json(json)
# print the JSON string representation of the object
print(ComboGroupDto.to_json())

# convert the object into a dict
combo_group_dto_dict = combo_group_dto_instance.to_dict()
# create an instance of ComboGroupDto from a dict
combo_group_dto_from_dict = ComboGroupDto.from_dict(combo_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


