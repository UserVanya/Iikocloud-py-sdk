# GetCountersResponse

Get counters response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**List[GuestCounter]**](GuestCounter.md) | Counters. | [optional] 

## Example

```python
from iikocloud_client.models.get_counters_response import GetCountersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCountersResponse from a JSON string
get_counters_response_instance = GetCountersResponse.from_json(json)
# print the JSON string representation of the object
print(GetCountersResponse.to_json())

# convert the object into a dict
get_counters_response_dict = get_counters_response_instance.to_dict()
# create an instance of GetCountersResponse from a dict
get_counters_response_from_dict = GetCountersResponse.from_dict(get_counters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


