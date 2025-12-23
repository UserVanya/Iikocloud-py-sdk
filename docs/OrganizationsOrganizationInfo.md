# OrganizationsOrganizationInfo

Organization details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** |  | 
**id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**name** | **str** | Organization name. | 
**code** | **str** | Organization&#x60;s code. | [optional] 
**external_data** | [**List[CommonExternalData]**](CommonExternalData.md) | Organization&#x60;s external data. | [optional] 

## Example

```python
from iikocloud_client.models.organizations_organization_info import OrganizationsOrganizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsOrganizationInfo from a JSON string
organizations_organization_info_instance = OrganizationsOrganizationInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationsOrganizationInfo.to_json())

# convert the object into a dict
organizations_organization_info_dict = organizations_organization_info_instance.to_dict()
# create an instance of OrganizationsOrganizationInfo from a dict
organizations_organization_info_from_dict = OrganizationsOrganizationInfo.from_dict(organizations_organization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


