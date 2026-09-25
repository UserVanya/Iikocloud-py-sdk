# NomenclatureGroupMarkupSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**markup_percent** | **float** | Markup percentage. Stored with up to 9 decimal places | [optional] 
**organization_id** | **UUID** | UUID of the organization (structural unit) | 

## Example

```python
from iikocloud_client.models.nomenclature_group_markup_setting import NomenclatureGroupMarkupSetting

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupMarkupSetting from a JSON string
nomenclature_group_markup_setting_instance = NomenclatureGroupMarkupSetting.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupMarkupSetting.to_json())

# convert the object into a dict
nomenclature_group_markup_setting_dict = nomenclature_group_markup_setting_instance.to_dict()
# create an instance of NomenclatureGroupMarkupSetting from a dict
nomenclature_group_markup_setting_from_dict = NomenclatureGroupMarkupSetting.from_dict(nomenclature_group_markup_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


