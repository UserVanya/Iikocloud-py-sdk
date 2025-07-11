# NetOrganizationGetProgramsResponse

Get programs response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**programs** | [**List[NetOrganizationLoyaltyProgram]**](NetOrganizationLoyaltyProgram.md) | Programs. | [optional] 

## Example

```python
from iikocloud_client.models.net_organization_get_programs_response import NetOrganizationGetProgramsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetOrganizationGetProgramsResponse from a JSON string
net_organization_get_programs_response_instance = NetOrganizationGetProgramsResponse.from_json(json)
# print the JSON string representation of the object
print(NetOrganizationGetProgramsResponse.to_json())

# convert the object into a dict
net_organization_get_programs_response_dict = net_organization_get_programs_response_instance.to_dict()
# create an instance of NetOrganizationGetProgramsResponse from a dict
net_organization_get_programs_response_from_dict = NetOrganizationGetProgramsResponse.from_dict(net_organization_get_programs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


