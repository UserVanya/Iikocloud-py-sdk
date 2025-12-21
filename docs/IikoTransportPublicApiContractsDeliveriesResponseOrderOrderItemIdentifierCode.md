# IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemIdentifierCode

OrderItem's IdentifierCode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id of order&#39;s position. | 
**code** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderIdentifierCode**](IikoTransportPublicApiContractsDeliveriesResponseOrderIdentifierCode.md) | Product code. | 
**flags** | **List[str]** | Application flags. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_order_item_identifier_code import IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemIdentifierCode

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemIdentifierCode from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_order_item_identifier_code_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemIdentifierCode.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemIdentifierCode.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_item_identifier_code_dict = iiko_transport_public_api_contracts_deliveries_response_order_order_item_identifier_code_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemIdentifierCode from a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_item_identifier_code_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemIdentifierCode.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_order_item_identifier_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


