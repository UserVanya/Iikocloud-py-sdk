# ConceptionGetByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier (UUID) | [optional] 

## Example

```python
from iikocloud_client.models.conception_get_by_id_request import ConceptionGetByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptionGetByIDRequest from a JSON string
conception_get_by_id_request_instance = ConceptionGetByIDRequest.from_json(json)
# print the JSON string representation of the object
print(ConceptionGetByIDRequest.to_json())

# convert the object into a dict
conception_get_by_id_request_dict = conception_get_by_id_request_instance.to_dict()
# create an instance of ConceptionGetByIDRequest from a dict
conception_get_by_id_request_from_dict = ConceptionGetByIDRequest.from_dict(conception_get_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


