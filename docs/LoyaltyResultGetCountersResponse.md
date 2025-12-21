# LoyaltyResultGetCountersResponse

Get counters response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**List[LoyaltyResultGuestCounter]**](LoyaltyResultGuestCounter.md) | Counters. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_get_counters_response import LoyaltyResultGetCountersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultGetCountersResponse from a JSON string
loyalty_result_get_counters_response_instance = LoyaltyResultGetCountersResponse.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultGetCountersResponse.to_json())

# convert the object into a dict
loyalty_result_get_counters_response_dict = loyalty_result_get_counters_response_instance.to_dict()
# create an instance of LoyaltyResultGetCountersResponse from a dict
loyalty_result_get_counters_response_from_dict = LoyaltyResultGetCountersResponse.from_dict(loyalty_result_get_counters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


