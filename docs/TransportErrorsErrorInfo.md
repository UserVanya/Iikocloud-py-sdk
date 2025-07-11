# TransportErrorsErrorInfo

DTO for error details transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**TransportErrorsErrorCode**](TransportErrorsErrorCode.md) | Error code. | 
**message** | **str** | Localized message. | [optional] 
**description** | **str** | Localized message. | [optional] 
**additional_data** | **object** | Additional information. | [optional] 

## Example

```python
from iikocloud_client.models.transport_errors_error_info import TransportErrorsErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportErrorsErrorInfo from a JSON string
transport_errors_error_info_instance = TransportErrorsErrorInfo.from_json(json)
# print the JSON string representation of the object
print(TransportErrorsErrorInfo.to_json())

# convert the object into a dict
transport_errors_error_info_dict = transport_errors_error_info_instance.to_dict()
# create an instance of TransportErrorsErrorInfo from a dict
transport_errors_error_info_from_dict = TransportErrorsErrorInfo.from_dict(transport_errors_error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


