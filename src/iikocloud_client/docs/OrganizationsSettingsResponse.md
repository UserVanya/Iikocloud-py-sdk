# OrganizationsSettingsResponse

Response to request for organizations specified settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[OrganizationSettings]**](OrganizationSettings.md) | List of organizations with specified settings. | 

## Example

```python
from iikocloud_client.models.organizations_settings_response import OrganizationsSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsSettingsResponse from a JSON string
organizations_settings_response_instance = OrganizationsSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationsSettingsResponse.to_json())

# convert the object into a dict
organizations_settings_response_dict = organizations_settings_response_instance.to_dict()
# create an instance of OrganizationsSettingsResponse from a dict
organizations_settings_response_from_dict = OrganizationsSettingsResponse.from_dict(organizations_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


