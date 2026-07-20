# InternalTransferSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.internal_transfer_save_response import InternalTransferSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferSaveResponse from a JSON string
internal_transfer_save_response_instance = InternalTransferSaveResponse.from_json(json)
# print the JSON string representation of the object
print(InternalTransferSaveResponse.to_json())

# convert the object into a dict
internal_transfer_save_response_dict = internal_transfer_save_response_instance.to_dict()
# create an instance of InternalTransferSaveResponse from a dict
internal_transfer_save_response_from_dict = InternalTransferSaveResponse.from_dict(internal_transfer_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


