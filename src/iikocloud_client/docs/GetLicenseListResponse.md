# GetLicenseListResponse

Request to obtain the information on license list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**organization_licenses** | [**List[OrganizationLicenseInfo]**](OrganizationLicenseInfo.md) | List of organization license information. | 

## Example

```python
from iikocloud_client.models.get_license_list_response import GetLicenseListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLicenseListResponse from a JSON string
get_license_list_response_instance = GetLicenseListResponse.from_json(json)
# print the JSON string representation of the object
print(GetLicenseListResponse.to_json())

# convert the object into a dict
get_license_list_response_dict = get_license_list_response_instance.to_dict()
# create an instance of GetLicenseListResponse from a dict
get_license_list_response_from_dict = GetLicenseListResponse.from_dict(get_license_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


