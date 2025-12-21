# CommonGetByOrganizationIdRequest

Get request only by organization id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | [optional] 

## Example

```python
from iikocloud_client.models.common_get_by_organization_id_request import CommonGetByOrganizationIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommonGetByOrganizationIdRequest from a JSON string
common_get_by_organization_id_request_instance = CommonGetByOrganizationIdRequest.from_json(json)
# print the JSON string representation of the object
print(CommonGetByOrganizationIdRequest.to_json())

# convert the object into a dict
common_get_by_organization_id_request_dict = common_get_by_organization_id_request_instance.to_dict()
# create an instance of CommonGetByOrganizationIdRequest from a dict
common_get_by_organization_id_request_from_dict = CommonGetByOrganizationIdRequest.from_dict(common_get_by_organization_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


