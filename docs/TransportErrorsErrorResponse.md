# TransportErrorsErrorResponse

Error response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**error_description** | **str** | Error text. | 
**error** | **str** | Error code. | [optional] 

## Example

```python
from iikocloud_client.models.transport_errors_error_response import TransportErrorsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportErrorsErrorResponse from a JSON string
transport_errors_error_response_instance = TransportErrorsErrorResponse.from_json(json)
# print the JSON string representation of the object
print(TransportErrorsErrorResponse.to_json())

# convert the object into a dict
transport_errors_error_response_dict = transport_errors_error_response_instance.to_dict()
# create an instance of TransportErrorsErrorResponse from a dict
transport_errors_error_response_from_dict = TransportErrorsErrorResponse.from_dict(transport_errors_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


