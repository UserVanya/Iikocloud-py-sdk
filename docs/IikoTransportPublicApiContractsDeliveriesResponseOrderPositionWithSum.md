# IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum

Order item positions with position discount sum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** | Order item position ID. | 
**sum** | **float** | Position discount sum. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_position_with_sum import IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_position_with_sum_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_position_with_sum_dict = iiko_transport_public_api_contracts_deliveries_response_order_position_with_sum_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum from a dict
iiko_transport_public_api_contracts_deliveries_response_order_position_with_sum_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_position_with_sum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


