# ConceptionListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** | Filter by deletion status; omit to return all records | [optional] 
**limit** | **int** | Maximum number of records (0 &#x3D; no limit) | [optional] 
**offset** | **int** | Number of records to skip | [optional] 
**revision** | **int** | Return only records with revision &gt;&#x3D; this value | [optional] 

## Example

```python
from iikocloud_client.models.conception_list_request import ConceptionListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptionListRequest from a JSON string
conception_list_request_instance = ConceptionListRequest.from_json(json)
# print the JSON string representation of the object
print(ConceptionListRequest.to_json())

# convert the object into a dict
conception_list_request_dict = conception_list_request_instance.to_dict()
# create an instance of ConceptionListRequest from a dict
conception_list_request_from_dict = ConceptionListRequest.from_dict(conception_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


