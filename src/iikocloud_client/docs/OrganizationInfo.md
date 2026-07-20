# OrganizationInfo

Organization details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Organization&#x60;s code. | [optional] 
**external_data** | [**List[CommonExternalData]**](CommonExternalData.md) | Organization&#x60;s external data. | [optional] 
**id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**name** | **str** | Organization name. | 
**response_type** | **str** |  | 

## Example

```python
from iikocloud_client.models.organization_info import OrganizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInfo from a JSON string
organization_info_instance = OrganizationInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationInfo.to_json())

# convert the object into a dict
organization_info_dict = organization_info_instance.to_dict()
# create an instance of OrganizationInfo from a dict
organization_info_from_dict = OrganizationInfo.from_dict(organization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


