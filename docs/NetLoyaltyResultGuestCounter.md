# NetLoyaltyResultGuestCounter

Guest counter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | Guest id. | [optional] 
**period** | [**IikoNetCommonEnumsCounterPeriod**](IikoNetCommonEnumsCounterPeriod.md) | Period. | [optional] 
**metric** | [**IikoNetCommonEnumsCounterMetric**](IikoNetCommonEnumsCounterMetric.md) | Metric. | [optional] 
**value** | **float** | Value. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_guest_counter import NetLoyaltyResultGuestCounter

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultGuestCounter from a JSON string
net_loyalty_result_guest_counter_instance = NetLoyaltyResultGuestCounter.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultGuestCounter.to_json())

# convert the object into a dict
net_loyalty_result_guest_counter_dict = net_loyalty_result_guest_counter_instance.to_dict()
# create an instance of NetLoyaltyResultGuestCounter from a dict
net_loyalty_result_guest_counter_from_dict = NetLoyaltyResultGuestCounter.from_dict(net_loyalty_result_guest_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


