# NomenclatureExternalMenu

External menu, related to ApiLogin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.nomenclature_external_menu import NomenclatureExternalMenu

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureExternalMenu from a JSON string
nomenclature_external_menu_instance = NomenclatureExternalMenu.from_json(json)
# print the JSON string representation of the object
print(NomenclatureExternalMenu.to_json())

# convert the object into a dict
nomenclature_external_menu_dict = nomenclature_external_menu_instance.to_dict()
# create an instance of NomenclatureExternalMenu from a dict
nomenclature_external_menu_from_dict = NomenclatureExternalMenu.from_dict(nomenclature_external_menu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


