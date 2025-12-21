# IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest

Get programs request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**without_marketing_campaigns** | **bool** | Determines if marketing campaigns not required. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request import IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request_instance = IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request_dict = iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest from a dict
iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request_from_dict = IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


