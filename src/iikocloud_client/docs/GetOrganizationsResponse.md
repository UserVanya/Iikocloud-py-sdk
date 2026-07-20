# GetOrganizationsResponse

Response to request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[OrganizationInfo]**](OrganizationInfo.md) | List of organizations.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_organizations_response import GetOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationsResponse from a JSON string
get_organizations_response_instance = GetOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationsResponse.to_json())

# convert the object into a dict
get_organizations_response_dict = get_organizations_response_instance.to_dict()
# create an instance of GetOrganizationsResponse from a dict
get_organizations_response_from_dict = GetOrganizationsResponse.from_dict(get_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


