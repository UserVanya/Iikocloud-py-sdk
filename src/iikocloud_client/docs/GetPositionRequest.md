# GetPositionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee position identifier (GUID) | [optional] 
**revision_from** | **int** | Revision from which to return changed records (optional) | [optional] 

## Example

```python
from iikocloud_client.models.get_position_request import GetPositionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPositionRequest from a JSON string
get_position_request_instance = GetPositionRequest.from_json(json)
# print the JSON string representation of the object
print(GetPositionRequest.to_json())

# convert the object into a dict
get_position_request_dict = get_position_request_instance.to_dict()
# create an instance of GetPositionRequest from a dict
get_position_request_from_dict = GetPositionRequest.from_dict(get_position_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


