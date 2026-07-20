# GetCounteragentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Number of records to return (1-500) | [optional] 
**offset** | **int** | Pagination offset | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | [optional] 
**type** | **List[str]** | Counteragent type (supplier, employee, client) | [optional] 

## Example

```python
from iikocloud_client.models.get_counteragents_request import GetCounteragentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCounteragentsRequest from a JSON string
get_counteragents_request_instance = GetCounteragentsRequest.from_json(json)
# print the JSON string representation of the object
print(GetCounteragentsRequest.to_json())

# convert the object into a dict
get_counteragents_request_dict = get_counteragents_request_instance.to_dict()
# create an instance of GetCounteragentsRequest from a dict
get_counteragents_request_from_dict = GetCounteragentsRequest.from_dict(get_counteragents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


