# OutgoingServiceSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_service_save_response import OutgoingServiceSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingServiceSaveResponse from a JSON string
outgoing_service_save_response_instance = OutgoingServiceSaveResponse.from_json(json)
# print the JSON string representation of the object
print(OutgoingServiceSaveResponse.to_json())

# convert the object into a dict
outgoing_service_save_response_dict = outgoing_service_save_response_instance.to_dict()
# create an instance of OutgoingServiceSaveResponse from a dict
outgoing_service_save_response_from_dict = OutgoingServiceSaveResponse.from_dict(outgoing_service_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


