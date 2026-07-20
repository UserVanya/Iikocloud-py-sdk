# ErrorInfo

DTO for error details transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **object** | Additional information. | [optional] 
**code** | [**ErrorCode**](ErrorCode.md) | Error code. | 
**description** | **str** | Localized message. | [optional] 
**error_reason** | **str** | Error reason. | [optional] 
**message** | **str** | Localized message. | [optional] 

## Example

```python
from iikocloud_client.models.error_info import ErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorInfo from a JSON string
error_info_instance = ErrorInfo.from_json(json)
# print the JSON string representation of the object
print(ErrorInfo.to_json())

# convert the object into a dict
error_info_dict = error_info_instance.to_dict()
# create an instance of ErrorInfo from a dict
error_info_from_dict = ErrorInfo.from_dict(error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


