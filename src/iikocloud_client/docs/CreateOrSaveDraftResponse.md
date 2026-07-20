# CreateOrSaveDraftResponse

Wrapping object (external) for a delivery order draft creation/update return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_id** | **UUID** | Order draft order ID. | 

## Example

```python
from iikocloud_client.models.create_or_save_draft_response import CreateOrSaveDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrSaveDraftResponse from a JSON string
create_or_save_draft_response_instance = CreateOrSaveDraftResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrSaveDraftResponse.to_json())

# convert the object into a dict
create_or_save_draft_response_dict = create_or_save_draft_response_instance.to_dict()
# create an instance of CreateOrSaveDraftResponse from a dict
create_or_save_draft_response_from_dict = CreateOrSaveDraftResponse.from_dict(create_or_save_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


