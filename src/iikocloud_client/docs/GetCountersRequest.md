# GetCountersRequest

Get counters request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_ids** | **List[UUID]** | Guest ids. | [optional] 
**metrics** | [**List[CounterMetric]**](CounterMetric.md) | Metrics. | [optional] 
**organization_id** | **UUID** | Organization id. | 
**periods** | [**List[CounterPeriod]**](CounterPeriod.md) | Periods. | [optional] 

## Example

```python
from iikocloud_client.models.get_counters_request import GetCountersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCountersRequest from a JSON string
get_counters_request_instance = GetCountersRequest.from_json(json)
# print the JSON string representation of the object
print(GetCountersRequest.to_json())

# convert the object into a dict
get_counters_request_dict = get_counters_request_instance.to_dict()
# create an instance of GetCountersRequest from a dict
get_counters_request_from_dict = GetCountersRequest.from_dict(get_counters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


