# IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType

Order type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**order_service_type** | [**IikoTransportPublicApiContractsDeliveriesCommonOrderServiceType**](IikoTransportPublicApiContractsDeliveriesCommonOrderServiceType.md) | Order type. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_order_type import IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_order_type_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_type_dict = iiko_transport_public_api_contracts_deliveries_response_order_order_type_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType from a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_type_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_order_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


