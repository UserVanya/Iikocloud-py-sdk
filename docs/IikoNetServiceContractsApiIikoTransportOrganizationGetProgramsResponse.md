# IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse

Get programs response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**programs** | [**List[IikoNetServiceContractsApiIikoTransportOrganizationLoyaltyProgram]**](IikoNetServiceContractsApiIikoTransportOrganizationLoyaltyProgram.md) | Programs. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_organization_get_programs_response import IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_organization_get_programs_response_instance = IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_organization_get_programs_response_dict = iiko_net_service_contracts_api_iiko_transport_organization_get_programs_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse from a dict
iiko_net_service_contracts_api_iiko_transport_organization_get_programs_response_from_dict = IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_organization_get_programs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


