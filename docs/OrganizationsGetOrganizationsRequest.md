# OrganizationsGetOrganizationsRequest

Request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which have to be returned. By default - all organizations from apiLogin.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**return_additional_info** | **bool** | A sign whether additional information about the organization should be returned (RMS version, country, restaurantAddress, etc.),    or only minimal information should be returned (id and name). | [optional] 
**include_disabled** | **bool** | Attribute that shows that response contains disabled organizations. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.organizations_get_organizations_request import OrganizationsGetOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsGetOrganizationsRequest from a JSON string
organizations_get_organizations_request_instance = OrganizationsGetOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationsGetOrganizationsRequest.to_json())

# convert the object into a dict
organizations_get_organizations_request_dict = organizations_get_organizations_request_instance.to_dict()
# create an instance of OrganizationsGetOrganizationsRequest from a dict
organizations_get_organizations_request_from_dict = OrganizationsGetOrganizationsRequest.from_dict(organizations_get_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


