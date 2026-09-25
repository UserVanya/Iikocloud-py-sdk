# StoresListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[FilterCondition]**](FilterCondition.md) | Filter conditions (AND-combined) | [optional] 
**limit** | **int** | Maximum number of records (0 &#x3D; no limit) | [optional] 
**offset** | **int** | Number of records to skip | [optional] 

## Example

```python
from iikocloud_client.models.stores_list_request import StoresListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoresListRequest from a JSON string
stores_list_request_instance = StoresListRequest.from_json(json)
# print the JSON string representation of the object
print(StoresListRequest.to_json())

# convert the object into a dict
stores_list_request_dict = stores_list_request_instance.to_dict()
# create an instance of StoresListRequest from a dict
stores_list_request_from_dict = StoresListRequest.from_dict(stores_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


