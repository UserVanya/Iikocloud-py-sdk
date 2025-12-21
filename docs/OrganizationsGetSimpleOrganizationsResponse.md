# OrganizationsGetSimpleOrganizationsResponse

Response to request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[OrganizationsSimpleOrganizationInfo]**](OrganizationsSimpleOrganizationInfo.md) | List of organizations.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.organizations_get_simple_organizations_response import OrganizationsGetSimpleOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsGetSimpleOrganizationsResponse from a JSON string
organizations_get_simple_organizations_response_instance = OrganizationsGetSimpleOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationsGetSimpleOrganizationsResponse.to_json())

# convert the object into a dict
organizations_get_simple_organizations_response_dict = organizations_get_simple_organizations_response_instance.to_dict()
# create an instance of OrganizationsGetSimpleOrganizationsResponse from a dict
organizations_get_simple_organizations_response_from_dict = OrganizationsGetSimpleOrganizationsResponse.from_dict(organizations_get_simple_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


