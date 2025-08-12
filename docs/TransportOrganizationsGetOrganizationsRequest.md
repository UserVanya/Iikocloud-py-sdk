# TransportOrganizationsGetOrganizationsRequest

Request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations IDs which have to be returned. By default - all organizations from apiLogin.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**return_additional_info** | **bool** | A sign whether additional information about the organization should be returned (RMS version, country, restaurantAddress, etc.),    or only minimal information should be returned (id and name). | [optional] 
**include_disabled** | **bool** | Attribute that shows that response contains disabled organizations. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.transport_organizations_get_organizations_request import TransportOrganizationsGetOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrganizationsGetOrganizationsRequest from a JSON string
transport_organizations_get_organizations_request_instance = TransportOrganizationsGetOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportOrganizationsGetOrganizationsRequest.to_json())

# convert the object into a dict
transport_organizations_get_organizations_request_dict = transport_organizations_get_organizations_request_instance.to_dict()
# create an instance of TransportOrganizationsGetOrganizationsRequest from a dict
transport_organizations_get_organizations_request_from_dict = TransportOrganizationsGetOrganizationsRequest.from_dict(transport_organizations_get_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


