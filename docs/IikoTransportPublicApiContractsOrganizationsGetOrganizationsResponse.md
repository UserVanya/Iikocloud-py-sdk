# IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse

Response to request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[IikoTransportPublicApiContractsOrganizationsOrganizationInfo]**](IikoTransportPublicApiContractsOrganizationsOrganizationInfo.md) | List of organizations.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_organizations_response import IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse from a JSON string
iiko_transport_public_api_contracts_organizations_get_organizations_response_instance = IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_organizations_get_organizations_response_dict = iiko_transport_public_api_contracts_organizations_get_organizations_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse from a dict
iiko_transport_public_api_contracts_organizations_get_organizations_response_from_dict = IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse.from_dict(iiko_transport_public_api_contracts_organizations_get_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


