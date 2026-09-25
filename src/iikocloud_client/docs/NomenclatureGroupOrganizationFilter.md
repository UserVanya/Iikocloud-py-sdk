# NomenclatureGroupOrganizationFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_excluding** | **bool** | Filter mode: false - the group is visible only in the listed organizations; true - visible everywhere except the listed organizations | [optional] 
**organization_ids** | **List[UUID]** | UUIDs of the organizations (structural units) to which the visibility filter applies | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_organization_filter import NomenclatureGroupOrganizationFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupOrganizationFilter from a JSON string
nomenclature_group_organization_filter_instance = NomenclatureGroupOrganizationFilter.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupOrganizationFilter.to_json())

# convert the object into a dict
nomenclature_group_organization_filter_dict = nomenclature_group_organization_filter_instance.to_dict()
# create an instance of NomenclatureGroupOrganizationFilter from a dict
nomenclature_group_organization_filter_from_dict = NomenclatureGroupOrganizationFilter.from_dict(nomenclature_group_organization_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


