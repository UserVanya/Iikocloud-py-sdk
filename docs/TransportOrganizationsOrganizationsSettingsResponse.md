# TransportOrganizationsOrganizationsSettingsResponse

Response to request for organizations specified settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**organizations** | [**List[TransportOrganizationsOrganizationSettings]**](TransportOrganizationsOrganizationSettings.md) | List of organizations with specified settings. | 

## Example

```python
from iikocloud_client.models.transport_organizations_organizations_settings_response import TransportOrganizationsOrganizationsSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrganizationsOrganizationsSettingsResponse from a JSON string
transport_organizations_organizations_settings_response_instance = TransportOrganizationsOrganizationsSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportOrganizationsOrganizationsSettingsResponse.to_json())

# convert the object into a dict
transport_organizations_organizations_settings_response_dict = transport_organizations_organizations_settings_response_instance.to_dict()
# create an instance of TransportOrganizationsOrganizationsSettingsResponse from a dict
transport_organizations_organizations_settings_response_from_dict = TransportOrganizationsOrganizationsSettingsResponse.from_dict(transport_organizations_organizations_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


