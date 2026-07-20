# OrganizationsSettingsRequest

Request for organizations specified settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_disabled** | **bool** | Attribute that shows that response contains disabled organizations. | [optional] 
**organization_ids** | **List[UUID]** | Organizations IDs which have to be returned. By default - all organizations from apiLogin. | [optional] 
**parameters** | [**List[OrganizationSettingsParameters]**](OrganizationSettingsParameters.md) | Parameters of information to be present in response. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.organizations_settings_request import OrganizationsSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsSettingsRequest from a JSON string
organizations_settings_request_instance = OrganizationsSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationsSettingsRequest.to_json())

# convert the object into a dict
organizations_settings_request_dict = organizations_settings_request_instance.to_dict()
# create an instance of OrganizationsSettingsRequest from a dict
organizations_settings_request_from_dict = OrganizationsSettingsRequest.from_dict(organizations_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


