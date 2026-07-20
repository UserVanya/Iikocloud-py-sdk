# IikoErrorResponse

Error response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**error** | **str** | Error code. | [optional] 
**error_description** | **str** | Error text. | 

## Example

```python
from iikocloud_client.models.iiko_error_response import IikoErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoErrorResponse from a JSON string
iiko_error_response_instance = IikoErrorResponse.from_json(json)
# print the JSON string representation of the object
print(IikoErrorResponse.to_json())

# convert the object into a dict
iiko_error_response_dict = iiko_error_response_instance.to_dict()
# create an instance of IikoErrorResponse from a dict
iiko_error_response_from_dict = IikoErrorResponse.from_dict(iiko_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


