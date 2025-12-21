# ComboGroupDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**is_main_group** | **bool** | Includes main dishes - these are the items around which the combo set is built. If a main dish is added to the order, the system can display a prompt &#39;build a combo set&#39;. | 
**items** | [**List[ComboGroupItemDto3]**](ComboGroupItemDto3.md) |  | [optional] 
**skip_step** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.combo_group_dto3 import ComboGroupDto3

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupDto3 from a JSON string
combo_group_dto3_instance = ComboGroupDto3.from_json(json)
# print the JSON string representation of the object
print(ComboGroupDto3.to_json())

# convert the object into a dict
combo_group_dto3_dict = combo_group_dto3_instance.to_dict()
# create an instance of ComboGroupDto3 from a dict
combo_group_dto3_from_dict = ComboGroupDto3.from_dict(combo_group_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


