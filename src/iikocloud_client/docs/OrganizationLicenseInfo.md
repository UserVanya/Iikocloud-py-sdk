# OrganizationLicenseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenses** | [**List[LicenseItem]**](LicenseItem.md) | List of licenses. | 
**organization_id** | **UUID** | Organization Id. | 

## Example

```python
from iikocloud_client.models.organization_license_info import OrganizationLicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLicenseInfo from a JSON string
organization_license_info_instance = OrganizationLicenseInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationLicenseInfo.to_json())

# convert the object into a dict
organization_license_info_dict = organization_license_info_instance.to_dict()
# create an instance of OrganizationLicenseInfo from a dict
organization_license_info_from_dict = OrganizationLicenseInfo.from_dict(organization_license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


