# NomenclatureProductMarkupSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**markup_percent** | **float** | Markup percentage. Stored with up to 9 decimal places | [optional] 
**organization_id** | **UUID** | UUID of the organization (structural unit) | 

## Example

```python
from iikocloud_client.models.nomenclature_product_markup_setting import NomenclatureProductMarkupSetting

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductMarkupSetting from a JSON string
nomenclature_product_markup_setting_instance = NomenclatureProductMarkupSetting.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductMarkupSetting.to_json())

# convert the object into a dict
nomenclature_product_markup_setting_dict = nomenclature_product_markup_setting_instance.to_dict()
# create an instance of NomenclatureProductMarkupSetting from a dict
nomenclature_product_markup_setting_from_dict = NomenclatureProductMarkupSetting.from_dict(nomenclature_product_markup_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


