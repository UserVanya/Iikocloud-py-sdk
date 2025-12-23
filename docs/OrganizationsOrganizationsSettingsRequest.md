# OrganizationsOrganizationsSettingsRequest

Request for organizations specified settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations IDs which have to be returned. By default - all organizations from apiLogin. | [optional] 
**include_disabled** | **bool** | Attribute that shows that response contains disabled organizations. | [optional] 
**parameters** | [**List[OrganizationsOrganizationSettingsParameters]**](OrganizationsOrganizationSettingsParameters.md) | Parameters of information to be present in response. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.organizations_organizations_settings_request import OrganizationsOrganizationsSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsOrganizationsSettingsRequest from a JSON string
organizations_organizations_settings_request_instance = OrganizationsOrganizationsSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationsOrganizationsSettingsRequest.to_json())

# convert the object into a dict
organizations_organizations_settings_request_dict = organizations_organizations_settings_request_instance.to_dict()
# create an instance of OrganizationsOrganizationsSettingsRequest from a dict
organizations_organizations_settings_request_from_dict = OrganizationsOrganizationsSettingsRequest.from_dict(organizations_organizations_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


