# ErrorsErrorInfo

DTO for error details transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ErrorsErrorCode**](ErrorsErrorCode.md) | Error code. | 
**message** | **str** | Localized message. | [optional] 
**description** | **str** | Localized message. | [optional] 
**additional_data** | **object** | Additional information. | [optional] 
**error_reason** | **str** | Error reason. | [optional] 

## Example

```python
from iikocloud_client.models.errors_error_info import ErrorsErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsErrorInfo from a JSON string
errors_error_info_instance = ErrorsErrorInfo.from_json(json)
# print the JSON string representation of the object
print(ErrorsErrorInfo.to_json())

# convert the object into a dict
errors_error_info_dict = errors_error_info_instance.to_dict()
# create an instance of ErrorsErrorInfo from a dict
errors_error_info_from_dict = ErrorsErrorInfo.from_dict(errors_error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


