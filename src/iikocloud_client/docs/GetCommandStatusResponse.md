# GetCommandStatusResponse

Class containing information about command status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 

## Example

```python
from iikocloud_client.models.get_command_status_response import GetCommandStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommandStatusResponse from a JSON string
get_command_status_response_instance = GetCommandStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetCommandStatusResponse.to_json())

# convert the object into a dict
get_command_status_response_dict = get_command_status_response_instance.to_dict()
# create an instance of GetCommandStatusResponse from a dict
get_command_status_response_from_dict = GetCommandStatusResponse.from_dict(get_command_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


