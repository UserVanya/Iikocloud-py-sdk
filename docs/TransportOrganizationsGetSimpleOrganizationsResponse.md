# TransportOrganizationsGetSimpleOrganizationsResponse

Response to request for organizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**organizations** | [**List[TransportOrganizationsSimpleOrganizationInfo]**](TransportOrganizationsSimpleOrganizationInfo.md) | List of organizations.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_organizations_get_simple_organizations_response import TransportOrganizationsGetSimpleOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrganizationsGetSimpleOrganizationsResponse from a JSON string
transport_organizations_get_simple_organizations_response_instance = TransportOrganizationsGetSimpleOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportOrganizationsGetSimpleOrganizationsResponse.to_json())

# convert the object into a dict
transport_organizations_get_simple_organizations_response_dict = transport_organizations_get_simple_organizations_response_instance.to_dict()
# create an instance of TransportOrganizationsGetSimpleOrganizationsResponse from a dict
transport_organizations_get_simple_organizations_response_from_dict = TransportOrganizationsGetSimpleOrganizationsResponse.from_dict(transport_organizations_get_simple_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


