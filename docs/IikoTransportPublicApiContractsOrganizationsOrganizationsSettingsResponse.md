# IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse

Response to request for organizations specified settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[IikoTransportPublicApiContractsOrganizationsOrganizationSettings]**](IikoTransportPublicApiContractsOrganizationsOrganizationSettings.md) | List of organizations with specified settings. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_organizations_settings_response import IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse from a JSON string
iiko_transport_public_api_contracts_organizations_organizations_settings_response_instance = IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_organizations_organizations_settings_response_dict = iiko_transport_public_api_contracts_organizations_organizations_settings_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse from a dict
iiko_transport_public_api_contracts_organizations_organizations_settings_response_from_dict = IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse.from_dict(iiko_transport_public_api_contracts_organizations_organizations_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


