# GetCounteragentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** | Filter by deletion flag: true — deleted only, false — non-deleted only, omit — all | [optional] 
**limit** | **int** | Number of records to return (1-500) | [optional] 
**offset** | **int** | Pagination offset | [optional] 
**revision** | **int** | Return only records with revision greater than or equal to the given value (revision &gt;&#x3D; value) | [optional] 
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


