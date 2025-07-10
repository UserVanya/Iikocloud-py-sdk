# NetLoyaltyResultGetCountersResponse

Get counters response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**List[NetLoyaltyResultGuestCounter]**](NetLoyaltyResultGuestCounter.md) | Counters. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_get_counters_response import NetLoyaltyResultGetCountersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultGetCountersResponse from a JSON string
net_loyalty_result_get_counters_response_instance = NetLoyaltyResultGetCountersResponse.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultGetCountersResponse.to_json())

# convert the object into a dict
net_loyalty_result_get_counters_response_dict = net_loyalty_result_get_counters_response_instance.to_dict()
# create an instance of NetLoyaltyResultGetCountersResponse from a dict
net_loyalty_result_get_counters_response_from_dict = NetLoyaltyResultGetCountersResponse.from_dict(net_loyalty_result_get_counters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


