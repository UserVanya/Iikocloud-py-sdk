# GetOrganizationsRequest

Request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_disabled** | **bool** | Attribute that shows that response contains disabled organizations. | [optional] 
**organization_ids** | **List[UUID]** | Organizations IDs which have to be returned. By default - all organizations from apiLogin.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**return_additional_info** | **bool** | A sign whether additional information about the organization should be returned (RMS version, country, restaurantAddress, etc.),    or only minimal information should be returned (id and name). | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.get_organizations_request import GetOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationsRequest from a JSON string
get_organizations_request_instance = GetOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationsRequest.to_json())

# convert the object into a dict
get_organizations_request_dict = get_organizations_request_instance.to_dict()
# create an instance of GetOrganizationsRequest from a dict
get_organizations_request_from_dict = GetOrganizationsRequest.from_dict(get_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


