# GetByOrganizationIdRequest

Get request only by organization id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | [optional] 

## Example

```python
from iikocloud_client.models.get_by_organization_id_request import GetByOrganizationIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetByOrganizationIdRequest from a JSON string
get_by_organization_id_request_instance = GetByOrganizationIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetByOrganizationIdRequest.to_json())

# convert the object into a dict
get_by_organization_id_request_dict = get_by_organization_id_request_instance.to_dict()
# create an instance of GetByOrganizationIdRequest from a dict
get_by_organization_id_request_from_dict = GetByOrganizationIdRequest.from_dict(get_by_organization_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


