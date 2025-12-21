# IikoTransportPublicApiContractsOrganizationsOrganizationInfo

Organization details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** |  | 
**id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**name** | **str** | Organization name. | 
**code** | **str** | Organization&#x60;s code. | [optional] 
**external_data** | [**List[IikoTransportPublicApiContractsCommonExternalData]**](IikoTransportPublicApiContractsCommonExternalData.md) | Organization&#x60;s external data. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_organization_info import IikoTransportPublicApiContractsOrganizationsOrganizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationInfo from a JSON string
iiko_transport_public_api_contracts_organizations_organization_info_instance = IikoTransportPublicApiContractsOrganizationsOrganizationInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrganizationsOrganizationInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_organizations_organization_info_dict = iiko_transport_public_api_contracts_organizations_organization_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationInfo from a dict
iiko_transport_public_api_contracts_organizations_organization_info_from_dict = IikoTransportPublicApiContractsOrganizationsOrganizationInfo.from_dict(iiko_transport_public_api_contracts_organizations_organization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


