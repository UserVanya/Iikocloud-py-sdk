# IncomingInventorySaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.incoming_inventory_save_response import IncomingInventorySaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventorySaveResponse from a JSON string
incoming_inventory_save_response_instance = IncomingInventorySaveResponse.from_json(json)
# print the JSON string representation of the object
print(IncomingInventorySaveResponse.to_json())

# convert the object into a dict
incoming_inventory_save_response_dict = incoming_inventory_save_response_instance.to_dict()
# create an instance of IncomingInventorySaveResponse from a dict
incoming_inventory_save_response_from_dict = IncomingInventorySaveResponse.from_dict(incoming_inventory_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


