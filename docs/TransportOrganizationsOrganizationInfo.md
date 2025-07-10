# TransportOrganizationsOrganizationInfo

Organization details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** |  | 
**id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**name** | **str** | Organization name. | 
**code** | **str** | Organization&#x60;s code. | [optional] 
**external_data** | [**List[TransportCommonExternalData]**](TransportCommonExternalData.md) | Organization&#x60;s external data. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_organizations_organization_info import TransportOrganizationsOrganizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrganizationsOrganizationInfo from a JSON string
transport_organizations_organization_info_instance = TransportOrganizationsOrganizationInfo.from_json(json)
# print the JSON string representation of the object
print(TransportOrganizationsOrganizationInfo.to_json())

# convert the object into a dict
transport_organizations_organization_info_dict = transport_organizations_organization_info_instance.to_dict()
# create an instance of TransportOrganizationsOrganizationInfo from a dict
transport_organizations_organization_info_from_dict = TransportOrganizationsOrganizationInfo.from_dict(transport_organizations_organization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


