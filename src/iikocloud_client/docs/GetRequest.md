# GetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the assembly chart | [optional] 

## Example

```python
from iikocloud_client.models.get_request import GetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRequest from a JSON string
get_request_instance = GetRequest.from_json(json)
# print the JSON string representation of the object
print(GetRequest.to_json())

# convert the object into a dict
get_request_dict = get_request_instance.to_dict()
# create an instance of GetRequest from a dict
get_request_from_dict = GetRequest.from_dict(get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


