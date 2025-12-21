# IikoNetServiceContractsApiIikoTransportLoyaltyResultGuestCounter

Guest counter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **UUID** | Guest id. | [optional] 
**period** | [**IikoNetCommonEnumsCounterPeriod**](IikoNetCommonEnumsCounterPeriod.md) | Period. | [optional] 
**metric** | [**IikoNetCommonEnumsCounterMetric**](IikoNetCommonEnumsCounterMetric.md) | Metric. | [optional] 
**value** | **float** | Value. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_guest_counter import IikoNetServiceContractsApiIikoTransportLoyaltyResultGuestCounter

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGuestCounter from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_guest_counter_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultGuestCounter.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultGuestCounter.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_guest_counter_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_guest_counter_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGuestCounter from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_guest_counter_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultGuestCounter.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_guest_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


