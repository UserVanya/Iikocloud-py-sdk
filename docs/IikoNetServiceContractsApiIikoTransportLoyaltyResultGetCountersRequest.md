# IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest

Get counters request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_ids** | **List[UUID]** | Guest ids. | [optional] 
**periods** | [**List[IikoNetCommonEnumsCounterPeriod]**](IikoNetCommonEnumsCounterPeriod.md) | Periods. | [optional] 
**metrics** | [**List[IikoNetCommonEnumsCounterMetric]**](IikoNetCommonEnumsCounterMetric.md) | Metrics. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


