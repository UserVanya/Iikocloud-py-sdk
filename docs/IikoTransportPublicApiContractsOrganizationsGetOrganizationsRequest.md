# IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest

Request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which have to be returned. By default - all organizations from apiLogin.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**return_additional_info** | **bool** | A sign whether additional information about the organization should be returned (RMS version, country, restaurantAddress, etc.),    or only minimal information should be returned (id and name). | [optional] 
**include_disabled** | **bool** | Attribute that shows that response contains disabled organizations. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_organizations_request import IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest from a JSON string
iiko_transport_public_api_contracts_organizations_get_organizations_request_instance = IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_organizations_get_organizations_request_dict = iiko_transport_public_api_contracts_organizations_get_organizations_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest from a dict
iiko_transport_public_api_contracts_organizations_get_organizations_request_from_dict = IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest.from_dict(iiko_transport_public_api_contracts_organizations_get_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


