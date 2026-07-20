# GetSimpleOrganizationsResponse

Response to request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organizations** | [**List[SimpleOrganizationInfo]**](SimpleOrganizationInfo.md) | List of organizations.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_simple_organizations_response import GetSimpleOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleOrganizationsResponse from a JSON string
get_simple_organizations_response_instance = GetSimpleOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSimpleOrganizationsResponse.to_json())

# convert the object into a dict
get_simple_organizations_response_dict = get_simple_organizations_response_instance.to_dict()
# create an instance of GetSimpleOrganizationsResponse from a dict
get_simple_organizations_response_from_dict = GetSimpleOrganizationsResponse.from_dict(get_simple_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


