# OrganizationsOrganizationsSettingsResponse

Response to request for organizations specified settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[OrganizationsOrganizationSettings]**](OrganizationsOrganizationSettings.md) | List of organizations with specified settings. | 

## Example

```python
from iikocloud_client.models.organizations_organizations_settings_response import OrganizationsOrganizationsSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsOrganizationsSettingsResponse from a JSON string
organizations_organizations_settings_response_instance = OrganizationsOrganizationsSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationsOrganizationsSettingsResponse.to_json())

# convert the object into a dict
organizations_organizations_settings_response_dict = organizations_organizations_settings_response_instance.to_dict()
# create an instance of OrganizationsOrganizationsSettingsResponse from a dict
organizations_organizations_settings_response_from_dict = OrganizationsOrganizationsSettingsResponse.from_dict(organizations_organizations_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


