# NomenclatureGroupDepartmentFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department_ids** | **List[str]** | UUIDs of the departments to which the visibility filter applies | [optional] 
**is_excluding** | **bool** | Filter mode: false - group is visible only in the listed departments; true - visible everywhere except the listed departments | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_department_filter import NomenclatureGroupDepartmentFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupDepartmentFilter from a JSON string
nomenclature_group_department_filter_instance = NomenclatureGroupDepartmentFilter.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupDepartmentFilter.to_json())

# convert the object into a dict
nomenclature_group_department_filter_dict = nomenclature_group_department_filter_instance.to_dict()
# create an instance of NomenclatureGroupDepartmentFilter from a dict
nomenclature_group_department_filter_from_dict = NomenclatureGroupDepartmentFilter.from_dict(nomenclature_group_department_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


