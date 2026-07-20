# GuestCounter

Guest counter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **UUID** | Guest id. | [optional] 
**metric** | [**CounterMetric**](CounterMetric.md) | Metric. | [optional] 
**period** | [**CounterPeriod**](CounterPeriod.md) | Period. | [optional] 
**value** | **float** | Value. | [optional] 

## Example

```python
from iikocloud_client.models.guest_counter import GuestCounter

# TODO update the JSON string below
json = "{}"
# create an instance of GuestCounter from a JSON string
guest_counter_instance = GuestCounter.from_json(json)
# print the JSON string representation of the object
print(GuestCounter.to_json())

# convert the object into a dict
guest_counter_dict = guest_counter_instance.to_dict()
# create an instance of GuestCounter from a dict
guest_counter_from_dict = GuestCounter.from_dict(guest_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


