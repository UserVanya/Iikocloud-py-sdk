# IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse

Response to request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[IikoTransportPublicApiContractsOrganizationsSimpleOrganizationInfo]**](IikoTransportPublicApiContractsOrganizationsSimpleOrganizationInfo.md) | List of organizations.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_simple_organizations_response import IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse from a JSON string
iiko_transport_public_api_contracts_organizations_get_simple_organizations_response_instance = IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_organizations_get_simple_organizations_response_dict = iiko_transport_public_api_contracts_organizations_get_simple_organizations_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse from a dict
iiko_transport_public_api_contracts_organizations_get_simple_organizations_response_from_dict = IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse.from_dict(iiko_transport_public_api_contracts_organizations_get_simple_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


