# NetOrganizationGetProgramsRequest

Get programs request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**without_marketing_campaigns** | **bool** | Determines if marketing campaigns not required. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_organization_get_programs_request import NetOrganizationGetProgramsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetOrganizationGetProgramsRequest from a JSON string
net_organization_get_programs_request_instance = NetOrganizationGetProgramsRequest.from_json(json)
# print the JSON string representation of the object
print(NetOrganizationGetProgramsRequest.to_json())

# convert the object into a dict
net_organization_get_programs_request_dict = net_organization_get_programs_request_instance.to_dict()
# create an instance of NetOrganizationGetProgramsRequest from a dict
net_organization_get_programs_request_from_dict = NetOrganizationGetProgramsRequest.from_dict(net_organization_get_programs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


