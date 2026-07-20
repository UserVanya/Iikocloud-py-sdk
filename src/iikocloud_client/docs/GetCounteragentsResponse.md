# GetCounteragentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counteragents** | [**List[Counteragent]**](Counteragent.md) | List of counteragents | [optional] 
**total_count** | **int** | Total number of counteragents | [optional] 

## Example

```python
from iikocloud_client.models.get_counteragents_response import GetCounteragentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCounteragentsResponse from a JSON string
get_counteragents_response_instance = GetCounteragentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetCounteragentsResponse.to_json())

# convert the object into a dict
get_counteragents_response_dict = get_counteragents_response_instance.to_dict()
# create an instance of GetCounteragentsResponse from a dict
get_counteragents_response_from_dict = GetCounteragentsResponse.from_dict(get_counteragents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


