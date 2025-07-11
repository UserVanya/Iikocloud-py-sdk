# NetLoyaltyResultGetCountersRequest

Get counters request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_ids** | **List[str]** | Guest ids. | [optional] 
**periods** | [**List[IikoNetCommonEnumsCounterPeriod]**](IikoNetCommonEnumsCounterPeriod.md) | Periods. | [optional] 
**metrics** | [**List[IikoNetCommonEnumsCounterMetric]**](IikoNetCommonEnumsCounterMetric.md) | Metrics. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_loyalty_result_get_counters_request import NetLoyaltyResultGetCountersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultGetCountersRequest from a JSON string
net_loyalty_result_get_counters_request_instance = NetLoyaltyResultGetCountersRequest.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultGetCountersRequest.to_json())

# convert the object into a dict
net_loyalty_result_get_counters_request_dict = net_loyalty_result_get_counters_request_instance.to_dict()
# create an instance of NetLoyaltyResultGetCountersRequest from a dict
net_loyalty_result_get_counters_request_from_dict = NetLoyaltyResultGetCountersRequest.from_dict(net_loyalty_result_get_counters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


