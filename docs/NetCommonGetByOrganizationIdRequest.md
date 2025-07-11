# NetCommonGetByOrganizationIdRequest

Get request only by organization id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization id. | [optional] 

## Example

```python
from iikocloud_client.models.net_common_get_by_organization_id_request import NetCommonGetByOrganizationIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCommonGetByOrganizationIdRequest from a JSON string
net_common_get_by_organization_id_request_instance = NetCommonGetByOrganizationIdRequest.from_json(json)
# print the JSON string representation of the object
print(NetCommonGetByOrganizationIdRequest.to_json())

# convert the object into a dict
net_common_get_by_organization_id_request_dict = net_common_get_by_organization_id_request_instance.to_dict()
# create an instance of NetCommonGetByOrganizationIdRequest from a dict
net_common_get_by_organization_id_request_from_dict = NetCommonGetByOrganizationIdRequest.from_dict(net_common_get_by_organization_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


