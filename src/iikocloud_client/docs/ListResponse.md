# ListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of assembly charts returned | [optional] 
**items** | [**List[AssemblyChartResponse]**](AssemblyChartResponse.md) | Ingredient lines of the assembly chart | [optional] 

## Example

```python
from iikocloud_client.models.list_response import ListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponse from a JSON string
list_response_instance = ListResponse.from_json(json)
# print the JSON string representation of the object
print(ListResponse.to_json())

# convert the object into a dict
list_response_dict = list_response_instance.to_dict()
# create an instance of ListResponse from a dict
list_response_from_dict = ListResponse.from_dict(list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


