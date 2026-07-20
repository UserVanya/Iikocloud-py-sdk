# GetCommandStatusRequest

Request for command status obtaining.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID obtained from any command supporting operations. | 
**organization_id** | **UUID** | Organization id which \&quot;correlationId\&quot; belongs to.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_command_status_request import GetCommandStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommandStatusRequest from a JSON string
get_command_status_request_instance = GetCommandStatusRequest.from_json(json)
# print the JSON string representation of the object
print(GetCommandStatusRequest.to_json())

# convert the object into a dict
get_command_status_request_dict = get_command_status_request_instance.to_dict()
# create an instance of GetCommandStatusRequest from a dict
get_command_status_request_from_dict = GetCommandStatusRequest.from_dict(get_command_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


