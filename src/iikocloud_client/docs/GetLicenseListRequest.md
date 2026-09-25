# GetLicenseListRequest

Request to obtain the information on license list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organization IDs for which license list information will be returned. By default - all organizations from API login. | [optional] 

## Example

```python
from iikocloud_client.models.get_license_list_request import GetLicenseListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetLicenseListRequest from a JSON string
get_license_list_request_instance = GetLicenseListRequest.from_json(json)
# print the JSON string representation of the object
print(GetLicenseListRequest.to_json())

# convert the object into a dict
get_license_list_request_dict = get_license_list_request_instance.to_dict()
# create an instance of GetLicenseListRequest from a dict
get_license_list_request_from_dict = GetLicenseListRequest.from_dict(get_license_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


