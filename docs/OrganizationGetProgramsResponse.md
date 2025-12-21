# OrganizationGetProgramsResponse

Get programs response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**programs** | [**List[OrganizationLoyaltyProgram]**](OrganizationLoyaltyProgram.md) | Programs. | [optional] 

## Example

```python
from iikocloud_client.models.organization_get_programs_response import OrganizationGetProgramsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGetProgramsResponse from a JSON string
organization_get_programs_response_instance = OrganizationGetProgramsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationGetProgramsResponse.to_json())

# convert the object into a dict
organization_get_programs_response_dict = organization_get_programs_response_instance.to_dict()
# create an instance of OrganizationGetProgramsResponse from a dict
organization_get_programs_response_from_dict = OrganizationGetProgramsResponse.from_dict(organization_get_programs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


