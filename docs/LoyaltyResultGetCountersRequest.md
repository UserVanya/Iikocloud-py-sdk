# LoyaltyResultGetCountersRequest

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
from iikocloud_client.models.loyalty_result_get_counters_request import LoyaltyResultGetCountersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultGetCountersRequest from a JSON string
loyalty_result_get_counters_request_instance = LoyaltyResultGetCountersRequest.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultGetCountersRequest.to_json())

# convert the object into a dict
loyalty_result_get_counters_request_dict = loyalty_result_get_counters_request_instance.to_dict()
# create an instance of LoyaltyResultGetCountersRequest from a dict
loyalty_result_get_counters_request_from_dict = LoyaltyResultGetCountersRequest.from_dict(loyalty_result_get_counters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


