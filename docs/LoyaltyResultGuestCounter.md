# LoyaltyResultGuestCounter

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
from iikocloud_client.models.loyalty_result_guest_counter import LoyaltyResultGuestCounter

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultGuestCounter from a JSON string
loyalty_result_guest_counter_instance = LoyaltyResultGuestCounter.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultGuestCounter.to_json())

# convert the object into a dict
loyalty_result_guest_counter_dict = loyalty_result_guest_counter_instance.to_dict()
# create an instance of LoyaltyResultGuestCounter from a dict
loyalty_result_guest_counter_from_dict = LoyaltyResultGuestCounter.from_dict(loyalty_result_guest_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


