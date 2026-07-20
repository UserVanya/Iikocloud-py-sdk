# ErrorCommandStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reason** | **str** | Error reason. | [optional] 
**exception** | **object** | Occured exception details. | [optional] 

## Example

```python
from iikocloud_client.models.error_command_status import ErrorCommandStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorCommandStatus from a JSON string
error_command_status_instance = ErrorCommandStatus.from_json(json)
# print the JSON string representation of the object
print(ErrorCommandStatus.to_json())

# convert the object into a dict
error_command_status_dict = error_command_status_instance.to_dict()
# create an instance of ErrorCommandStatus from a dict
error_command_status_from_dict = ErrorCommandStatus.from_dict(error_command_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


