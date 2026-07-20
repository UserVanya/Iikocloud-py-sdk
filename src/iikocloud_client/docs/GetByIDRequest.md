# GetByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | 
**organization_id** | **str** | Organization identifier (GUID) | 

## Example

```python
from iikocloud_client.models.get_by_id_request import GetByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetByIDRequest from a JSON string
get_by_id_request_instance = GetByIDRequest.from_json(json)
# print the JSON string representation of the object
print(GetByIDRequest.to_json())

# convert the object into a dict
get_by_id_request_dict = get_by_id_request_instance.to_dict()
# create an instance of GetByIDRequest from a dict
get_by_id_request_from_dict = GetByIDRequest.from_dict(get_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


