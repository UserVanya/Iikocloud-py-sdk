# OrganizationGetProgramsRequest

Get programs request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**without_marketing_campaigns** | **bool** | Determines if marketing campaigns not required. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.organization_get_programs_request import OrganizationGetProgramsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGetProgramsRequest from a JSON string
organization_get_programs_request_instance = OrganizationGetProgramsRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationGetProgramsRequest.to_json())

# convert the object into a dict
organization_get_programs_request_dict = organization_get_programs_request_instance.to_dict()
# create an instance of OrganizationGetProgramsRequest from a dict
organization_get_programs_request_from_dict = OrganizationGetProgramsRequest.from_dict(organization_get_programs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


