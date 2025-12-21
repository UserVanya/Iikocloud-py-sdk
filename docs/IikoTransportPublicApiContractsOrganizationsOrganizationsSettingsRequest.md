# IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest

Request for organizations specified settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which have to be returned. By default - all organizations from apiLogin. | [optional] 
**include_disabled** | **bool** | Attribute that shows that response contains disabled organizations. | [optional] 
**parameters** | [**List[IikoTransportPublicApiContractsOrganizationsOrganizationSettingsParameters]**](IikoTransportPublicApiContractsOrganizationsOrganizationSettingsParameters.md) | Parameters of information to be present in response. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_organizations_settings_request import IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest from a JSON string
iiko_transport_public_api_contracts_organizations_organizations_settings_request_instance = IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_organizations_organizations_settings_request_dict = iiko_transport_public_api_contracts_organizations_organizations_settings_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest from a dict
iiko_transport_public_api_contracts_organizations_organizations_settings_request_from_dict = IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest.from_dict(iiko_transport_public_api_contracts_organizations_organizations_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


